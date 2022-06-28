from django import forms
from .models import Expense

class ExpenseModelForm(forms.ModelForm):
    class Meta:
        model = Expense
        #fields = ('name', 'price') #顯示特定欄位
        fields = '__all__' #顯示所有欄位
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'})
        }
        labels = {
            'name': '花費項目',
            'price': '金額'
        }