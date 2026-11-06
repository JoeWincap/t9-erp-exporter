from . import specs
from .template import T9PureTemplate

class T9Exporter:
    """高階匯出窗口：自動字典對齊並呼叫純渲染器"""

    @staticmethod
    def _map(records, spec):
        rows = []
        sorted_spec = sorted(spec, key=lambda x: x["col"])
        for item in records:
            row = [item.get(rule["src"], rule.get("default", "")) for rule in sorted_spec]
            rows.append(row)
        return rows

    @classmethod
    def export_so(cls, file_path, header_data, body_data):
        """傳入字典串列，匯開發貨單 (SO)"""
        h_rows = cls._map(header_data, specs.SO_HEADER_MAPPING)
        b_rows = cls._map(body_data, specs.SO_BODY_MAPPING)
        T9PureTemplate.render_so(file_path, h_rows, b_rows)

    @classmethod
    def export_po(cls, file_path, header_data, body_data):
        """傳入字典串列，匯開採購單 (PO)"""
        h_rows = cls._map(header_data, specs.PO_HEADER_MAPPING)
        b_rows = cls._map(body_data, specs.PO_BODY_MAPPING)
        T9PureTemplate.render_po(file_path, h_rows, b_rows)