from django.contrib import admin
from django.forms.models import BaseInlineFormSet
from .models import Article
from .models import Scope
from .models import Tag
from django.core.exceptions import ValidationError



class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        new_list=[]
        for form in self.forms:
            new_list.append((form.cleaned_data.get('is_main')))
            if new_list.count(True) == 0:
                raise ValidationError('Один раздел должен быть основным!')
            elif new_list.count(True) > 1:
                raise ValidationError('Ошибка!')
        return super().clean()

#
class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]

