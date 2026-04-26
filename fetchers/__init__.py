"""
公司新聞爬蟲
"""

from .base import CompanyFetcher, CompanyDocument

from .applied_materials import AppliedMaterialsFetcher
from .auo import AuoFetcher
from .boe import BoeFetcher
from .canon import CanonFetcher
from .corning import CorningFetcher
from .csot import CsotFetcher
from .himax import HimaxFetcher
from .innolux import InnoluxFetcher
from .jdi import JdiFetcher
from .lg_display import LgDisplayFetcher
from .lg_elec import LgElecFetcher
from .novatek import NovatekFetcher
from .raydium import RaydiumFetcher
from .samsung_elec import SamsungElecFetcher
from .sony import SonyFetcher
from .tcl import TclFetcher
from .vizio import VizioFetcher

FETCHERS = {
    "applied_materials": AppliedMaterialsFetcher,
    "auo": AuoFetcher,
    "boe": BoeFetcher,
    "canon": CanonFetcher,
    "corning": CorningFetcher,
    "csot": CsotFetcher,
    "himax": HimaxFetcher,
    "innolux": InnoluxFetcher,
    "jdi": JdiFetcher,
    "lg_display": LgDisplayFetcher,
    "lg_elec": LgElecFetcher,
    "novatek": NovatekFetcher,
    "raydium": RaydiumFetcher,
    "samsung_elec": SamsungElecFetcher,
    "sony": SonyFetcher,
    "tcl": TclFetcher,
    "vizio": VizioFetcher,
}
