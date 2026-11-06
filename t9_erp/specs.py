# =========================================================================
# 發貨單 (SO) 規格定義
# =========================================================================
SO_HEADER_NOTES = [
    "這是發貨單號", "做發貨單的日期", "郁高=1000\n威愷=2000", "固定SC", "固定1000",
    "直接客戶=DC\n同行=DS", "", "負責業務", "內銷=TWD\n外銷=交易幣別", "固定1",
    "內銷=1 \n外銷=匯率", "內銷=5 \n外銷=0", "內銷=國內訂單 \n外銷=跟客人談好的", "真正出貨日期"
]

SO_HEADER_FIELDS = [
    "單據編號", "單據日期", "銷售公司代碼", "單據類型", "銷售組織",
    "銷售通路", "客戶代碼", "業務人員代碼", "交易幣別", "原幣匯率值",
    "本幣匯率值", "稅代碼", "貿易條件", "DATE OF DEPARTAURE"
]

SO_HEADER_MAPPING = [
    {"col": 0, "src": "order_no", "default": ""},
    {"col": 1, "src": "order_date", "default": ""},
    {"col": 2, "src": "seller_code", "default": 1000},
    {"col": 3, "src": "doc_type", "default": "SC"},
    {"col": 4, "src": "sales_org", "default": 1000},
    {"col": 5, "src": "channel", "default": "DS"},
    {"col": 6, "src": "buyer_code", "default": 2000},
    {"col": 7, "src": "staff_code", "default": "W057"},
    {"col": 8, "src": "currency", "default": "TWD"},
    {"col": 9, "src": "fx_orig", "default": 1},
    {"col": 10, "src": "fx_local", "default": 1},
    {"col": 11, "src": "tax_code", "default": 5},
    {"col": 12, "src": "trade_term", "default": "Z"},
    {"col": 13, "src": "ship_date", "default": ""},
]

SO_BODY_NOTES = [
    "固定1000", "郁高=1000\n威愷=2000", "出貨數量", "內銷=5 \n外銷=0", "這是發貨單號",
    "", "發貨單的序號", "固定0", "MPN", "CPN", "固定KPCS", "出貨數量",
    "出貨單價", "備註", "這才是訂單編號", "可以都放1", "裝箱編號", "PO儲位"
]

SO_BODY_FIELDS = [
    "供貨組織代碼", "供貨公司代碼", "發貨數量", "稅代碼", "單據編號",
    "標識號", "序號", "類型", "產品代碼", "原廠編號(規格型號)",
    "交易單位代碼", "發貨數量", "交易價", "備註", "銷售訂單號碼",
    "銷售訂單序號", "裝箱編號", "PO儲位"
]

SO_BODY_MAPPING = [
    {"col": 0, "src": "supply_org", "default": 1000},
    {"col": 1, "src": "seller_code", "default": 1000},
    {"col": 2, "src": "qty_kpcs", "default": 0.0},
    {"col": 3, "src": "tax_code", "default": 5},
    {"col": 4, "src": "order_no", "default": ""},
    {"col": 5, "src": "flag_id", "default": ""},
    {"col": 6, "src": "seq_no", "default": ""},
    {"col": 7, "src": "item_type", "default": ""},
    {"col": 8, "src": "part_no", "default": ""},
    {"col": 9, "src": "spec_model", "default": ""},
    {"col": 10, "src": "unit", "default": "KPCS"},
    {"col": 11, "src": "qty_kpcs", "default": 0.0},
    {"col": 12, "src": "price", "default": 0.0},
    {"col": 13, "src": "remark", "default": ""},
    {"col": 14, "src": "so_no", "default": ""},
    {"col": 15, "src": "so_seq", "default": 1},
    {"col": 16, "src": "pack_no", "default": ""},
    {"col": 17, "src": "po_cell", "default": ""},
]

# =========================================================================
# 採購單 (PO) 規格定義
# =========================================================================
PO_HEADER_NOTES = [
    "", "", "", "固定=1000", "固定=1000", "廠商代碼", "本次交易幣別",
    "可不維護由系統取數", "", "人員代碼", "同F欄位", "稅碼代碼",
    "固定=1000", "公司的記帳幣別", "公司代碼", "公司代碼"
]

PO_HEADER_FIELDS = [
    "單據編號", "單據日期", "單據類型", "採購組織", "核算組織",
    "供應商", "交易幣別", "原貨幣值", "目的貨幣值", "採購人員代碼",
    "債權方", "稅碼", "債務組織", "債務組織交易幣別", "採購公司", "債務公司"
]

PO_HEADER_MAPPING = [
    {"col": 0, "src": "order_no", "default": ""},
    {"col": 1, "src": "order_date", "default": ""},
    {"col": 2, "src": "doc_type", "default": "AP"},
    {"col": 3, "src": "pur_org", "default": 1000},
    {"col": 4, "src": "acc_org", "default": 1000},
    {"col": 5, "src": "seller_code", "default": 2000},
    {"col": 6, "src": "currency", "default": "TWD"},
    {"col": 7, "src": "fx_orig", "default": 1},
    {"col": 8, "src": "fx_dest", "default": 1},
    {"col": 9, "src": "staff_code", "default": "W057"},
    {"col": 10, "src": "seller_code", "default": 2000},
    {"col": 11, "src": "tax_code", "default": 5},
    {"col": 12, "src": "debt_org", "default": 1000},
    {"col": 13, "src": "currency", "default": "TWD"},
    {"col": 14, "src": "buyer_code", "default": 1000},
    {"col": 15, "src": "buyer_code", "default": 1000},
]

PO_BODY_NOTES = [
    "固定=1000", "同[基本資訊]_L欄位", "廠商回覆的交期", "固定=1000", "固定=1000",
    "公司代碼", "公司代碼", "同[基本資訊]_A欄位", "產品=0\n費用=1",
    "產品代碼或是費用代碼", "", "", "", "", "", ""
]

PO_BODY_FIELDS = [
    "需求組織代碼", "稅代碼", "交貨日期", "收貨組織代碼", "債務組織代碼",
    "收貨公司", "需求公司", "單據編號", "類型", "產品代碼",
    "產品名稱", "交易數量", "交易價", "金額", "規格型號", "備註"
]

PO_BODY_MAPPING = [
    {"col": 0, "src": "req_org", "default": 1000},
    {"col": 1, "src": "tax_code", "default": 5},
    {"col": 2, "src": "order_date", "default": ""},
    {"col": 3, "src": "recv_org", "default": 1000},
    {"col": 4, "src": "debt_org", "default": 1000},
    {"col": 5, "src": "buyer_code", "default": 1000},
    {"col": 6, "src": "buyer_code", "default": 1000},
    {"col": 7, "src": "order_no", "default": ""},
    {"col": 8, "src": "item_type", "default": ""},
    {"col": 9, "src": "part_no", "default": ""},
    {"col": 10, "src": "part_name", "default": ""},
    {"col": 11, "src": "qty_kpcs", "default": 0.0},
    {"col": 12, "src": "price", "default": 0.0},
    {"col": 13, "src": "amount", "default": 0.0},
    {"col": 14, "src": "spec_model", "default": ""},
    {"col": 15, "src": "remark", "default": ""},
]