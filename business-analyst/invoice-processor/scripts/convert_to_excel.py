#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Convert invoice recognition JSON results to formatted Excel spreadsheet
"""

import json
import argparse
import os
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side


def main():
    """主函数"""
    # 解析命令行参数
    parser = argparse.ArgumentParser(description='Convert invoice JSON results to Excel')
    parser.add_argument('-i', '--input', default='invoice_results.json',
                        help='Input JSON file (default: invoice_results.json)')
    parser.add_argument('-o', '--output', default='invoice_results.xlsx',
                        help='Output Excel file (default: invoice_results.xlsx)')
    args = parser.parse_args()

    # 读取 JSON 文件
    with open(args.input, 'r', encoding='utf-8') as f:
        data = json.load(f)

    wb = Workbook()
    detail_sheet = wb.active
    detail_sheet.title = '发票明细'

    # 设置标题样式
    header_fill = PatternFill(start_color='4472C4', end_color='4472C4', fill_type='solid')
    header_font = Font(bold=True, color='FFFFFF', size=12)
    border = Border(
        left=Side(style='thin'),
        right=Side(style='thin'),
        top=Side(style='thin'),
        bottom=Side(style='thin')
    )

    # 设置表头
    headers = [
        '序号', '文件路径', '状态', '发票类型', '发票号码', '开票日期',
        '购买方名称', '销售方名称', '合计金额(不含税)', '合计税额',
        '价税合计', '项目名称'
    ]

    for col, header in enumerate(headers, start=1):
        cell = detail_sheet.cell(row=1, column=col, value=header)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = Alignment(horizontal='center', vertical='center')
        cell.border = border

    # 填充数据
    for idx, result in enumerate(data['results'], start=2):
        detail_sheet.cell(row=idx, column=1, value=idx-1)

        file_path = result.get('file_path', '')
        detail_sheet.cell(row=idx, column=2, value=file_path)

        status = result.get('status', '')
        status_cell = detail_sheet.cell(row=idx, column=3, value=status)
        if status == 'success':
            status_cell.font = Font(color='008000')
        else:
            status_cell.font = Font(color='FF0000')

        invoice_data = result.get('data', {})

        detail_sheet.cell(row=idx, column=4, value=invoice_data.get('invoice_type'))
        detail_sheet.cell(row=idx, column=5, value=invoice_data.get('invoice_number'))
        detail_sheet.cell(row=idx, column=6, value=invoice_data.get('invoice_date'))
        detail_sheet.cell(row=idx, column=7, value=invoice_data.get('buyer_name'))
        detail_sheet.cell(row=idx, column=8, value=invoice_data.get('seller_name'))

        # 金额字段
        amount_exc = invoice_data.get('total_amount_excluding_tax')
        if amount_exc:
            detail_sheet.cell(row=idx, column=9, value=float(amount_exc))
            detail_sheet.cell(row=idx, column=9).number_format = '#,##0.00'

        tax = invoice_data.get('total_tax')
        if tax:
            detail_sheet.cell(row=idx, column=10, value=float(tax))
            detail_sheet.cell(row=idx, column=10).number_format = '#,##0.00'

        amount_inc = invoice_data.get('total_amount_including_tax')
        if amount_inc:
            detail_sheet.cell(row=idx, column=11, value=float(amount_inc))
            detail_sheet.cell(row=idx, column=11).number_format = '#,##0.00'

        # 项目名称
        item_names = invoice_data.get('item_names', [])
        detail_sheet.cell(row=idx, column=12, value=', '.join(item_names) if item_names else '')

        # 应用边框
        for col in range(1, 13):
            detail_sheet.cell(row=idx, column=col).border = border
            detail_sheet.cell(row=idx, column=col).alignment = Alignment(vertical='center')

    # 调整列宽
    column_widths = [8, 35, 10, 15, 22, 12, 30, 30, 18, 12, 15, 40]
    for idx, width in enumerate(column_widths, start=1):
        detail_sheet.column_dimensions[detail_sheet.cell(row=1, column=idx).column_letter].width = width

    # 冻结首行
    detail_sheet.freeze_panes = 'A2'

    wb.save(args.output)
    print(f'Excel 文件已创建: {args.output}')

    # 删除输入的 JSON 文件
    try:
        if os.path.exists(args.input):
            os.remove(args.input)
            print(f'已删除临时文件: {args.input}')
    except Exception as e:
        print(f'警告: 无法删除临时文件 {args.input}: {e}')


if __name__ == '__main__':
    main()
