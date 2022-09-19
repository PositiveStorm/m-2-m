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
            # raise ValidationError('Тут всегда ошибка')
        return super().clean()  # вызываем базовый код переопределяемого метода

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

