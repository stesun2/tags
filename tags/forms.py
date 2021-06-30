from django import forms

class TagForm(forms.Form):
    # The name of this variable becomes the name of the input in the form, as well as
    # the "id_"-prefixed value of the label's "for" attribute...
    #
    # <label for="id_tag" ...
    # <input name="tag" ...
    tag = forms.CharField(label='Enter tag:', max_length=20)

