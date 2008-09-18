<h2>Edit ceiling</h2>

<&| @zookeepr.lib.form:fill, defaults=defaults, errors=errors &>

<% h.form(h.url(id=c.ceiling.id)) %>
<& form.myt &>
<p><% h.submitbutton('Update') %> <% h.link_to('back', url=h.url(action='index', id=None)) %></p>
<% h.end_form() %>

</&>

<%args>
defaults
errors
</%args>

<%init>
if not defaults and c.ceiling:
    defaults = {
        'ceiling.name': c.ceiling.name,
        'ceiling.max_sold': c.ceiling.max_sold,
        'ceiling.available_from': c.ceiling.available_from,
        'ceiling.available_until': c.ceiling.available_until,
    }
</%init>
