from email.mime import image
from datetime import datetime
from odoo import models
import base64
import io


class PurchaseByThinhXlsx(models.AbstractModel):
    _name = 'report.my_purchase.order_template_my_purchase_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def add_company_header(self, row, sheet, company, bold):
        address = company.street
        city = company.city
        phone = company.phone
        email = company.email

        if company.logo:
            image_data = io.BytesIO(base64.b64decode(company.logo))
            sheet.insert_image(
                row + 1, 15, 'logo.png', {'image_data': image_data, 'x_scale': 0.2, 'y_scale': 0.2})

            sheet.write(row, 1, address)
            sheet.write(row+1, 1, city)
            sheet.write(row + 2, 1, phone)
            sheet.write(row + 3, 1, email)

    # can chinh phan delivery_address
    def add_company_delivery_address(self, row, workbook, sheet, company):
        name = company.name
        address = f"{company.street} {company.city}"
        phone = company.phone
        cell_format = workbook.add_format({"font_size": 10})
        cell_format_contenchild = workbook.add_format({"font_size": 11})
        cell_format.set_text_wrap()

        sheet.merge_range("C10:D10", 'NAME')
        sheet.merge_range("E10:I10", '.')
        sheet.merge_range("C11:D11", '.')
        sheet.merge_range("E11:I11", '.')
        sheet.merge_range("C12:D12", '.')
        sheet.merge_range("E12:I12", '.')
        sheet.set_row(row, 25)
        sheet.set_row(row + 1, 25)
        sheet.set_row(row + 2, 25)

        sheet.write(row, 2, "NAME COMPANY", cell_format_contenchild)
        sheet.write(row, 4, name, cell_format)
        sheet.write(row + 1, 2, "ADDRESS", cell_format_contenchild)
        sheet.write(row + 1, 4, address, cell_format)
        sheet.write(row + 2, 2, "TEL", cell_format_contenchild)
        sheet.write(row + 2, 4, phone, cell_format)

    def generate_xlsx_report(self, workbook, data, orders):
        row = 0
        for order in orders:

            sheet = workbook.add_worksheet(order.name)
            # sheet.set_default_row(18)
            bold = workbook.add_format({"bold": True})
            fontsize_namePurchase = workbook.add_format({"font_size": 20})
            merge_formatcontent = workbook.add_format(
                {'align': 'center', "font_size": 18})
            merge_formatcontent.set_underline()
            merge_formatcontentchild = workbook.add_format(
                {'align': 'left', "font_size": 14})
            merge_formatcontentchild.set_underline()
            format_th = workbook.add_format(
                {"font_size": 12, "align": "left", 'underline': True})

            white_bg = workbook.add_format({'bg_color': 'white'})
            bottom_border = workbook.add_format({'bottom': True})
            left_border = workbook.add_format({'left': True})

            cell_format_term = workbook.add_format({"font_size": 11})
            cell_format_term.set_text_wrap()
            date_format = workbook.add_format({'num_format': 'mmmm d yyyy',"align": "left"})

            number_format = workbook.add_format({'num_format': '#,##0.00',"align": "left"})
            sheet.set_column('E:E',25)

            company = self.env.company
            self.add_company_header(row, sheet, company, bold)
            sheet.set_row(row+1, 25)
            sheet.write(row + 1, 9, order.name, fontsize_namePurchase)
            row += 6
            # sheet.write(row,1,"test ne")
            sheet.set_row(row, 30)
            sheet.merge_range(
                "G7:M7", 'PURCHASE REQUEST QUOTATION', merge_formatcontent)  # 6
            row += 2
            # sheet.write(row,1,"test tiep ne")
            sheet.set_row(row+8, 30)
            sheet.merge_range("C9:F9", 'DELIVERY ADDRESS',
                              merge_formatcontentchild)
            sheet.merge_range("K9:O9", 'VENDOR ADDRESS',
                              merge_formatcontentchild)
            row += 1

            self.add_company_delivery_address(row, workbook, sheet, company)

            # can chinh phan VENDOR ADDRESS
            cell_format2 = workbook.add_format({"font_size": 10})
            cell_format_contenchild2 = workbook.add_format({"font_size": 11})
            cell_format2.set_text_wrap()
            sheet.merge_range("K10:L10", 'NAME')
            sheet.merge_range("M10:P10", '.')
            sheet.merge_range("K11:L11", '.')
            sheet.merge_range("M11:P11", '.')
            sheet.merge_range("K12:L12", '.')
            sheet.merge_range("M12:P12", '.')
            color_bg = workbook.add_format(
                {'bg_color': '#009879', 'font_color': '#ffffff'})
            if order.partner_id:
                for item in order.partner_id:
                    sheet.write(row, 10, 'NAME COMPANY',
                                cell_format_contenchild2)
                    sheet.write(row, 12, item.name, cell_format2)

                    sheet.write(row+1, 10, 'ADDRESS', cell_format_contenchild2)
                    sheet.write(row + 1, 12, item.street, cell_format2)

                    sheet.write(row+2, 10, 'TEL', cell_format_contenchild2)
                    sheet.write(row + 2, 12, item.phone, cell_format2)

            row += 6
            sheet.set_row(row, 25)
            sheet.merge_range("C16:H16", 'PLEASE MAKE ALL PAYMENTS TO:',
                              merge_formatcontentchild)
            sheet.merge_range("K16:O16", 'TERMS AND CONDITIONS:',
                              merge_formatcontentchild)
            row += 1
            sheet.merge_range("C17:D17", 'NAME')
            sheet.merge_range("E17:I17", '.')

            sheet.merge_range("C18:D18", '.')
            sheet.merge_range("E18:I18", '.')

            sheet.merge_range("C19:D19", '.')
            sheet.merge_range("E19:I19", '.')

            sheet.merge_range("C20:D20", '.')
            sheet.merge_range("E20:I20", '.')

            sheet.merge_range("C21:D21", '.')
            sheet.merge_range("E21:I21", '.')

            if order.partner_id:
                for item2 in order.partner_id:
                    if item2.bank_ids:
                        for line in item2.bank_ids:
                            if line.bank_id:
                                for bank in line.bank_id:
                                    name = company.name
                                    account = f"{line.acc_number} {item2.currency_id.name}"
                                    account_name = bank.name
                                    sheet.write(row, 2, 'ACCOUNT NAME:')
                                    sheet.write(row, 4, name)

                                    sheet.write(row + 1, 2, 'ACCOUNT NO:')
                                    sheet.write(row + 1, 4, account)

                                    sheet.write(row + 2, 2, 'SWIFT CODE:')
                                    sheet.write(row + 2, 4, 'SCA214312')

                                    sheet.write(row + 3, 2, 'BANK NAME:')
                                    sheet.write(row + 3, 4, account_name)

                                    sheet.write(row + 4, 2, 'ADDRESS:')
                                    sheet.write(row + 4, 4, 'street')
            if order.notes:
                sheet.merge_range("K17:P24", '.')
                sheet.write(row, 10, order.notes, cell_format_term)

            row += 6
            sheet.merge_range("B23:D24", '.')
            sheet.merge_range("E24:L24", '.')
            for line in order.order_line:
                if line.product_id:
                    descrip = line.name
                    dilivery = line.date_planned
                    date = datetime.strptime(
                        str(dilivery), "%Y-%m-%d %H:%M:%S").date()

                    for product in line.product_id:
                        productname = product.name
                    for taxes in line.taxes_id:
                        taxesname = taxes.name
                        # sheet.write(row,1,,color_bg)
                        sheet.merge_range(row, 1, row, 3, 'Name')
                        sheet.merge_range(row, 4, row, 11, 'Descriptions')
                        # sheet.write(row,4,'Descriptions',color_bg )

                        sheet.merge_range(row + 1, 1, row+1, 3, 'PRODUCT NAME')
                        sheet.merge_range(row + 1, 4, row + 1, 11, productname)

                        sheet.merge_range(row + 2, 1, row + 2, 3, 'DESCRIPTION')
                        sheet.merge_range(row + 2, 4, row + 2, 11, descrip)
                        image_data = io.BytesIO(
                            base64.b64decode(product.image_1920))
                        sheet.insert_image(
                            row + 2, 13, product.image_1920, {'image_data': image_data, 'x_scale': 0.1, 'y_scale': 0.1})
                        sheet.merge_range(row + 3, 1, row + 3, 3, 'TAXES')
                        sheet.merge_range(row + 3, 4, row + 3, 11, taxesname)

                        sheet.merge_range(row + 4, 1, row + 4, 3, 'DELIVERY DATE')
                        # sheet.write_datetime(row + 4, 4, row + 4, 11, date, date_format)
                        sheet.write_datetime(row +4 , 4, date, date_format)

                        sheet.merge_range(row + 5,  1, row + 5, 3, 'QUANTITY')
                        sheet.merge_range(row + 5,  4, row + 5, 11, line.product_qty,number_format)

                        sheet.merge_range(row + 6,  1, row + 6, 3, 'UNIT PRICE (USD)')
                        sheet.merge_range(row + 6,  4, row + 6, 11, line.price_unit,number_format)

                        sheet.merge_range(row + 7,  1, row + 7, 3, 'AMOUNT (USD)')
                        sheet.merge_range(row + 7,  4, row + 7, 11, line.price_subtotal,number_format)
                        row += 1

                row += 8
            row += 2
            sheet.merge_range(row, 6, row, 8, 'TOTAL')
            sheet.merge_range(row, 9, row, 11, order.amount_untaxed,number_format)

            sheet.merge_range(row + 1, 6, row + 1, 8, 'TAXES')
            sheet.merge_range(row + 1, 9, row + 1, 11, order.amount_tax,number_format)

            sheet.merge_range(row+2, 6, row+2, 8, 'SHIPPING COST')
            sheet.merge_range(row + 2, 9, row + 2, 11, '13998')

            sheet.merge_range(row + 3, 6, row+3, 8, 'PALLETS')
            sheet.merge_range(row + 3, 9, row + 3, 11, '250')

            sheet.merge_range(row+4, 6, row+4, 8, 'GRAND TOTAL')
            sheet.merge_range(row + 4, 9, row + 4, 11, order.amount_total,number_format)

            sheet.conditional_format(
                f"A1:R{row+7}", {'type': 'formula', 'criteria': 'True', 'format': white_bg})
            sheet.conditional_format(
                f"A{row+7}:R{row+7}", {'type': 'formula', 'criteria': 'True', 'format': bottom_border})
            sheet.conditional_format(
                f"S1:S{row+7}", {'type': 'formula', 'criteria': 'True', 'format': left_border})
