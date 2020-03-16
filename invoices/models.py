from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from phonenumber_field.modelfields import PhoneNumberField


# class InvoiceManager(models.Manager):
#     def get_invoice_items(self):
#         return self.items.all()


class Client(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    company = models.CharField(max_length=100)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    phone_number = PhoneNumberField(blank=True)

    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)

    def get_absolute_url(self):
        return reverse("client-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return f"Client: {self.first_name} {self.last_name}"


class Invoice(models.Model):

    title = models.CharField(max_length=200)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    # description = models.TextField()
    invoice_total = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, editable=False
    )
    create_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name: "Invoice"
        verbose_name_plural: "Invoices"  # noqa F821

    def get_absolute_url(self):
        return reverse("invoice-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.title} - {self.invoice_total}"

    def __repr__(self):
        return f"<Invoice: {self.client} - {self.title}>"

    # @property
    def get_invoice_total(self):
        # return f'${self.invoice_total}'
        total = 0
        total = sum([item.subtotal() for item in self.items.all()])
        # self.invoice_total = total
        return total

    def save(self, *args, **kwargs):
        #  TODO: Figure out why this doesn't always work
        self.invoice_total = self.get_invoice_total()
        super().save(*args, **kwargs)


class InvoiceItem(models.Model):
    # Invoice Line Items
    invoice = models.ForeignKey(Invoice, related_name="items", on_delete=models.CASCADE)
    item = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    rate = models.DecimalField(max_digits=6, decimal_places=2)
    tax = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    class Meta:
        verbose_name: "Invoice Item"
        verbose_name_plural: "Invoice Items"

    def __str__(self):
        # return self.item
        return f"{self.item} - {self.subtotal()}"

    def __repr__(self):
        return f"<Invoice Line Item: {self.item} - {self.subtotal()}>"

    def subtotal(self):
        return self.quantity * self.rate

    def save(self, *args, **kwargs):
        # Add a call to update invoice total here
        # When creating new invoices in the django admin,
        # invoice totals are not calculated
        # super().save(*args, **kwargs)
        # self.invoice.get_invoice_total()

        # super().save(*args, **kwargs)
        self.invoice.save()
        super().save(*args, **kwargs)
