import smtplib

from formencode import validators
from formencode.schema import Schema
from formencode.variabledecode import NestedVariables

from zookeepr.lib.base import *
from zookeepr.lib.validators import BaseSchema, ProposalTypeValidator, FileUploadValidator
from zookeepr.model import Person, ProposalType, Proposal, Attachment
    
class RegistrationSchema(Schema):
    email_address = validators.String(not_empty=True)
    password = validators.String(not_empty=True)
    password_confirm = validators.String(not_empty=True)
    fullname = validators.String()

class ProposalSchema(Schema):
    title = validators.String(not_empty=True)
    abstract = validators.String(not_empty=True)
    type = ProposalTypeValidator()
    experience = validators.String()
    url = validators.String()
    assistance = validators.Bool()
    
class NewCFPSchema(BaseSchema):
    registration = RegistrationSchema()
    proposal = ProposalSchema()
    attachment = FileUploadValidator()
    pre_validators = [NestedVariables]

class CfpController(BaseController):
    def index(self):
        return render_response("cfp/list.myt")

    def submit(self):
        c.cfptypes = Query(ProposalType).select()

        errors = {}
        defaults = dict(request.POST)

        if request.method == 'POST' and defaults:
            result, errors = NewCFPSchema().validate(defaults)

            if not errors:
                c.proposal = Proposal()
                # update the objects with the validated form data
                for k in result['proposal']:
                    setattr(c.proposal, k, result['proposal'][k])
                
                c.registration = Person()
                for k in result['registration']:
                    setattr(c.registration, k, result['registration'][k])
                c.registration.proposals.append(c.proposal)

                if result['attachment'] is not None:
                    c.attachment = Attachment()
                    for k in result['attachment']:
                        setattr(c.attachment, k, result['attachment'][k])
                    c.proposal.attachments.append(c.attachment)

                s = smtplib.SMTP("localhost")
                # generate the message from a template
                body = render('cfp/submission_response.myt', id=c.registration.url_hash, fragment=True)
                s.sendmail("seven-contact@lca2007.linux.org.au", c.registration.email_address, body)
                s.quit()

                return render_response('cfp/thankyou.myt')

        # unmangle the errors
        good_errors = {}
        for key in errors.keys():
            for subkey in errors[key].keys():
                good_errors[key + "." + subkey] = errors[key][subkey]

        return render_response("cfp/new.myt", defaults=defaults, errors=good_errors)
