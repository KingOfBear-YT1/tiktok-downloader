from .snaptik import snaptik, Snaptik
from .ssstik import ssstik
from .scrapper import VideoInfo
from .tikmate import tikmate, Tikmate
from .mdown import mdown, Mdown
from .Except import InvalidUrl
from .ttdownloader import ttdownloader, TTDownloader
from .tikdown import tikdown, Tikdown

__all__ = [
    'snaptik',
    'Snaptik',
    'ssstik',
    'VideoInfo',
    'tikmate',
    'Tikmate',
    'mdown',
    'Mdown',
    'InvalidUrl',
    'ttdownloader',
    'tikdown',
    'Tikdown',
    'TTDownloader'
]
services = {
    'snaptik': snaptik,
    'ssstik': ssstik,
    'tikmate': tikmate,
    'mdown': mdown,
    'ttdownloader': ttdownloader,
    'tikdown': tikdown,
    'tiktok': VideoInfo.service
}
