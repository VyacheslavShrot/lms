from django import forms

from groups.models import Group


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = (
            "group_name",
            "amount_students",
            "head_teacher",
            "faculty",
            "head_teacher_email",
            "head_teacher_phone",
        )

    def clean_group_name(self):
        group_name = self.cleaned_data["group_name"].upper()
        return group_name

    def clean_faculty(self):
        faculty = self.cleaned_data["faculty"].capitalize()
        return faculty


class GroupAdminForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = "__all__"

    comments = forms.CharField(required=False, widget=forms.Textarea)
    email = forms.EmailField()
    send_email = forms.BooleanField()

    def save(self, commit=True):
        print(self.cleaned_data["email"])
        return super().save(commit=commit)
