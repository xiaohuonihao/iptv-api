import os
import re

from utils.i18n import t

config_dir = "config"

output_dir = "output"

live_path = os.path.join(config_dir, "live")

hls_path = os.path.join(config_dir, "hls")

local_dir_path = os.path.join(config_dir, "local")

local_path = os.path.join(config_dir, "local.txt")

channel_logo_path = os.path.join(config_dir, "logo")

alias_path = os.path.join(config_dir, "alias.txt")

epg_path = os.path.join(config_dir, "epg.txt")

whitelist_path = os.path.join(config_dir, "whitelist.txt")

blacklist_path = os.path.join(config_dir, "blacklist.txt")

subscribe_path = os.path.join(config_dir, "subscribe.txt")

epg_result_path = os.path.join(output_dir, "epg/epg.xml")

epg_gz_result_path = os.path.join(output_dir, "epg/epg.gz")

ipv4_result_path = os.path.join(output_dir, "ipv4/result.txt")

ipv6_result_path = os.path.join(output_dir, "ipv6/result.txt")

live_result_path = os.path.join(output_dir, "live.txt")

live_ipv4_result_path = os.path.join(output_dir, "ipv4/live.txt")

live_ipv6_result_path = os.path.join(output_dir, "ipv6/live.txt")

rtmp_data_path = os.path.join(output_dir, "data/rtmp.db")

hls_result_path = os.path.join(output_dir, "hls.txt")

hls_ipv4_result_path = os.path.join(output_dir, "ipv4/hls.txt")

hls_ipv6_result_path = os.path.join(output_dir, "ipv6/hls.txt")

cache_path = os.path.join(output_dir, "data/cache.gz")

frozen_path = os.path.join(output_dir, "data/frozen.gz")

speed_test_log_path = os.path.join(output_dir, "log/speed_test.log")

result_log_path = os.path.join(output_dir, "log/result.log")

statistic_log_path = os.path.join(output_dir, "log/statistic.log")

unmatch_log_path = os.path.join(output_dir, "log/unmatch.log")

log_path = os.path.join(output_dir, "log/log.log")

url_host_pattern = re.compile(r"((https?|rtmp|rtsp)://)?([^:@/]+(:[^:@/]*)?@)?(\[[0-9a-fA-F:]+]|([\w-]+\.)+[\w-]+)")

url_pattern = re.compile(
    r"(?P<url>" + url_host_pattern.pattern + r"\S*)")

rt_url_pattern = re.compile(r"^(rtmp|rtsp)://.*$")

rtp_pattern = re.compile(r"^(?P<name>[^,，]+)[,，]?(?P<url>rtp://.*)$")
# 将这行 (新版本):
# demo_txt_pattern = re.compile(r"^(?P<name>[^,，]+)[,，]?(?!#genre#)(?P<value>.+)?$")

# 替换为 (老版本):
demo_txt_pattern = re.compile(r"^(?P<name>[^,，]+)[,，]?(?!#genre#)" + r"(" + url_pattern.pattern + r")?")

txt_pattern = re.compile(r"^(?P<name>[^,，]+)[,，](?!#genre#)(?P<value>.+)$")

multiline_txt_pattern = re.compile(r"^(?P<name>[^,，]+)[,，](?!#genre#)(?P<value>.+)$", re.MULTILINE)

m3u_pattern = re.compile(r"^#EXTINF:-1[\s+,，](?P<attributes>[^,，]+)[，,](?P<name>.*?)\n(?P<value>.+)$")

multiline_m3u_pattern = re.compile(
    r"^#EXTINF:-1(?:[\s+,，]*(?P<attributes>(?:[^,，\r\n\"]+|\"[^\"\r\n]*\")*))?[,，](?P<name>.*?)[\r\n]+"
    r"(?P<options>(?:(?:[ \t]*\r?\n)+|#EXTVLCOPT:[^\r\n]*(?:\r?\n|$))*)(?P<value>.*?)(?=\r?\n(?:[ \t]*\r?\n)*#EXTINF:-1|\Z)",
    re.MULTILINE | re.DOTALL)

key_value_pattern = re.compile(r'(?P<key>[\w-]+)=(?P<value>"[^"]*"|\'[^\']*\'|\S+)')

sub_pattern = re.compile(
    r"-|_|\((.*?)\)|（(.*?)）|\[(.*?)]|「(.*?)」| |｜|频道|普清|标清|高清|HD|hd|超清|超高|超高清|4K|4k|中央|央视|电视台|台|电信|联通|移动")

replace_dict = {
    "plus": "+",
    "PLUS": "+",
    "＋": "+",
}

region_list = [
    "广东",
    "北京",
    "湖南",
    "湖北",
    "浙江",
    "上海",
    "天津",
    "江苏",
    "山东",
    "河南",
    "河北",
    "山西",
    "陕西",
    "安徽",
    "重庆",
    "福建",
    "江西",
    "辽宁",
    "黑龙江",
    "吉林",
    "四川",
    "云南",
    "香港",
    "内蒙古",
    "甘肃",
    "海南",
    "云南",
]

origin_map = {
    "hotel": "酒店源",
    "multicast": "组播源",
    "subscribe": t("name.subscribe"),
    "online_search": "关键字源",
    "whitelist": t("name.whitelist"),
    "local": t("name.local"),
}

ipv6_proxy = "http://www.ipv6proxy.net/go.php?u="

foodie_url = "http://www.foodieguide.com/iptvsearch/"

foodie_hotel_url = "http://www.foodieguide.com/iptvsearch/hoteliptv.php"

waiting_tip = t("msg.waiting_tip")
