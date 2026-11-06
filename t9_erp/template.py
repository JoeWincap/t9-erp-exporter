import os
import xlsxwriter
from . import specs

class T9PureTemplate:
    """T9 純格式渲染模板：接收二維串列，產生合規 Excel"""

    BASE_FONT = {'font_name': '微軟正黑體', 'font_size': 10}

    @staticmethod
    def _create_styles(wb):
        return {
            "title": wb.add_format({**T9PureTemplate.BASE_FONT, 'bold': True, 'align': 'center', 'valign': 'vcenter'}),
            "note": wb.add_format({**T9PureTemplate.BASE_FONT, 'font_size': 8}),
            "header": wb.add_format({
                **T9PureTemplate.BASE_FONT, 'bold': True, 'underline': 2,
                'bg_color': '#FF0000', 'font_color': '#FFFFFF', 'border': 1
            }),
            "text": wb.add_format({**T9PureTemplate.BASE_FONT, 'num_format': '@'}),
            "int": wb.add_format({**T9PureTemplate.BASE_FONT, 'num_format': '0'}),
            "num": wb.add_format({**T9PureTemplate.BASE_FONT, 'num_format': '#,##0.0000'})
        }

    @classmethod
    def write_sheet(cls, ws, title, notes, headers, rows, styles):
        col_count = len(headers)

        ws.merge_range(0, 0, 0, col_count - 1, "", styles["title"])
        ws.merge_range(1, 0, 1, col_count - 1, title, styles["title"])

        for c, v in enumerate(notes):
            ws.write(2, c, v, styles["note"])
        for c, v in enumerate(headers):
            ws.write(3, c, v, styles["header"])

        for r_idx, row in enumerate(rows, start=4):
            if len(row) != col_count:
                raise ValueError(f"[{title}] 第 {r_idx + 1} 列長度不符！預期 {col_count} 欄，實際 {len(row)} 欄。")

            for c_idx, val in enumerate(row):
                if isinstance(val, float):
                    fmt = styles["num"]
                    clean_val = val
                elif isinstance(val, int) and not isinstance(val, bool):
                    fmt = styles["int"]
                    clean_val = val
                else:
                    fmt = styles["text"]
                    clean_val = "" if val is None else str(val)

                ws.write(r_idx, c_idx, clean_val, fmt)

    @classmethod
    def render_so(cls, file_path, header_rows, body_rows):
        dir_name = os.path.dirname(os.path.abspath(file_path))
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)

        wb = xlsxwriter.Workbook(file_path)
        styles = cls._create_styles(wb)

        ws_h = wb.add_worksheet("發貨單－基本資訊0")
        cls.write_sheet(ws_h, "發貨單", specs.SO_HEADER_NOTES, specs.SO_HEADER_FIELDS, header_rows, styles)

        ws_b = wb.add_worksheet("發貨單－表身明細1")
        cls.write_sheet(ws_b, "發貨單", specs.SO_BODY_NOTES, specs.SO_BODY_FIELDS, body_rows, styles)

        wb.close()

    @classmethod
    def render_po(cls, file_path, header_rows, body_rows):
        dir_name = os.path.dirname(os.path.abspath(file_path))
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)

        wb = xlsxwriter.Workbook(file_path)
        styles = cls._create_styles(wb)

        ws_h = wb.add_worksheet("採購訂單－基本資訊0")
        cls.write_sheet(ws_h, "採購訂單", specs.PO_HEADER_NOTES, specs.PO_HEADER_FIELDS, header_rows, styles)

        ws_b = wb.add_worksheet("採購訂單－明細資料1")
        cls.write_sheet(ws_b, "採購訂單", specs.PO_BODY_NOTES, specs.PO_BODY_FIELDS, body_rows, styles)

        wb.close()