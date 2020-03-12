from pyecharts import GeoLines, Style
from pyecharts import Map
import pyecharts.constants as constants

# https://github.com/pyecharts/pyecharts/blob/master/pyecharts/charts/geolines.py
style = Style(
    title_top="#fff",
    title_pos = "center",
    width=1000,
    height=500,
    background_color="#404a59"
)


# 特效图形的标记。有 'circle', 'rect', 'roundRect', 'triangle', 'diamond','pin', 'arrow', 'plane' 可选。
style_geo = style.add(
    maptype="海南",
    is_label_show=True,
    line_curve=0.2,#线条曲度
    line_opacity=0.6,
    legend_text_color="#eee",#图例文字颜色
    legend_pos="right",#图例位置
    geo_effect_symbol="pin",#特效形状
    geo_effect_symbolsize=15,#特效大小
    label_color=['#a6c84c', '#ffa022', '#46bee9'],
    label_pos="right",
    label_formatter="{b}",#//标签内容格式器
    label_text_color="#eee",
)

data_guangzhou = [
    ['三亚', '海口'],
    ['文昌市', '海口'],
    ['文昌市', '琼海'],
    ['海口', '万宁市'],
    ['文昌市', '三亚'],
    ['琼海', '万宁市'],
    ['文昌市', '万宁市'],
    ['海口', '琼海'],
    ['三亚', '琼海'],
    ['三亚', '万宁市'],
    ['海口', '儋州市'],
    ['万宁市', '儋州市'],
    ['琼海', '儋州市'],
    ['三亚', '儋州市'],
    ['文昌市', '儋州市'],
]
geolines = GeoLines("GeoLines", **style.init_style)
geolines.add("海南旅游轨迹", data_guangzhou, **style_geo)
geolines.render('地理线图.html')

