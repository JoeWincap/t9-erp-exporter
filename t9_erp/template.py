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
    def _write_sheet(cls, ws, title, notes, headers, rows, styles):
        """通用工作表繪製器：負責固定格式的表頭與動態資料列寫入"""
        col_count = len(headers)
        
        # 1. 標題區 (Row 0 ~ 1)
        ws.merge_range(0, 0, 0, col_count - 1, "", styles["title"])
        ws.merge_range(1, 0, 1, col_count - 1, title, styles["title"])
        
        # 2. 備註與欄位名稱 (Row 2 ~ 3)
        for c, v in enumerate(notes): 
            ws.write(2, c, v, styles["note"])
        for c, v in enumerate(headers): 
            ws.write(3, c, v, styles["header"])

        # 3. 資料列 (Row 4 起)
        for r_idx, row in enumerate(rows, start=4):
            # -------------------------------------------------------------
            # ★ 位置 1：欄位長度防呆 (防未來自己寫業務腳本時漏拼欄位)
            # -------------------------------------------------------------
            if len(row) != col_count:
                raise ValueError(f"[{title}] 第 {r_idx + 1} 列欄位數量錯誤！預期 {col_count} 欄，實際傳入 {len(row)} 欄。資料內容：{row}")

            for c_idx, val in enumerate(row):
                # -------------------------------------------------------------
                # ★ 位置 2：自動處理 None、去除空白與抹除隱形 .0
                # -------------------------------------------------------------
                if isinstance(val, float):
                    fmt = styles["num"]
                    clean_val = val
                elif isinstance(val, int) and not isinstance(val, bool):
                    fmt = styles["int"]
                    clean_val = val
                else:
                    fmt = styles["text"]
                    if val is None:
                        clean_val = ""
                    else:
                        # 自動脫水 + 將結尾的 .0 斬草除根
                        clean_val = re.sub(r'\.0$', '', str(val).strip())

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