import datetime
from StringIO import StringIO

from pyboleto.bank.itau import BoletoItau
from pyboleto.pdf import BoletoPDF

from django.utils.translation import ugettext as _

from gunclub import settings


def generate_invoice_pdf(due_date, value, user, profile):
    pdf_buffer = StringIO()

    boleto_pdf = BoletoPDF(pdf_buffer)
    d = BoletoItau()

    d.carteira = settings.CLUB_BANK_PORTFOLIO
    d.cedente = settings.CLUB_NAME
    d.cedente_documento = settings.CLUB_CNPJ
    d.cedente_endereco = settings.CLUB_ADDRESS
    d.agencia_cedente = settings.CLUB_BANK_AGENCY
    d.conta_cedente = settings.CLUB_BANK_ACCOUNT
    d.data_vencimento = due_date
    d.data_documento = datetime.date.today()
    d.data_processamento = datetime.date.today()
    d.valor = value
    d.valor_documento = d.valor
    d.nosso_numero = settings.CLUB_BANK_OUR_NUMBER
    d.numero_documento = d.nosso_numero
    d.instrucoes = settings.CLUB_CASHIER_INSTRUCTIONS
    d.demonstrativo = [
        _('MONTHLY FEE FOR MONTH %(month)s/%(year)s') % {
            'month': due_date.month,
            'year': due_date.year},
    ]
    d.sacado = [
        "%s %s" % (user.first_name, user.last_name),
        "%s %s" % (profile.street, profile.postal_code),
        "%s %s %s" % (profile.street2, profile.city, profile.state_province)
    ]

    boleto_pdf.drawBoleto(d)
    boleto_pdf.save()

    return pdf_buffer.getvalue()
