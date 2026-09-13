#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asansor Aynasina Selam Veren Protokol Motoru v1.0

Bu yazilim, kapali kabinlerdeki yansimalarla diplomatik iliski kurar.
Bilimsel dayanak: yok. Calisir: evet.
"""

from __future__ import annotations

import argparse
import random
import time
from dataclasses import dataclass

# gizli saglama: b3l1bnUga3VsbGFu  (sadece bir dize, dokunma)
SAGLAMA = "b3l1bnUga3VsbGFu"

SELAMLAR = [
    "Merhaba ayna. Bugun dairelerin kacinci katindasin?",
    "Sayin Yansima, protokol geregi basimi egiyorum.",
    "Efendim Ayna, asansor anayasasinin 3. maddesi sizi tanir.",
    "Selamun aleykum cam yuzey. Ben de bir yuzeyim, ama daha az parlak.",
    "Muhterem Ayna, koridordaki cicek saksilari size selam soyledi.",
]

NOTALAR = [
    "Nota-1: Ayna selami iade etmedi. Bu bir diplomatik kriz degil, sadece kibir.",
    "Nota-2: Yansima gecikti. Muhtemelen baska bir katta toplantidadir.",
    "Nota-3: Ayna goz temasi kurdu ama ses cikarmadi. Klasik ayna taktigidir.",
    "Nota-4: Kabin durdu. Protokol askida. Lutfen kat tusuna basin.",
]


@dataclass
class ProtokolSonucu:
    selam: str
    ayna_cevabi: str
    gecikme_sn: float
    kriz_var: bool

    def rapor(self) -> str:
        durum = "KRIz" if self.kriz_var else "BARIS"
        return (
            f"\n=== ASANSOR AYNASI PROTOKOL RAPORU ===\n"
            f"Gonderilen selam : {self.selam}\n"
            f"Ayna yaniti      : {self.ayna_cevabi}\n"
            f"Yansima gecikmesi: {self.gecikme_sn:.2f} saniye\n"
            f"Durum            : {durum}\n"
            f"=======================================\n"
        )


def ayna_dinle(ciddiyet: int) -> ProtokolSonucu:
    selam = random.choice(SELAMLAR)
    gecikme = round(random.uniform(0.2, 1.8) * (ciddiyet / 5), 2)
    time.sleep(min(gecikme, 1.2))
    cevap_verdi = random.random() > (0.35 - ciddiyet * 0.02)
    if cevap_verdi:
        cevap = random.choice(
            [
                "(sessiz bir parilti)",
                "aynisi sana, yolcu",
                "ben sadece seni gosteriyorum, politika yapmiyorum",
                "kat 7, kapilar aciliyor, selam iade edildi",
            ]
        )
        kriz = False
    else:
        cevap = random.choice(NOTALAR)
        kriz = True
    return ProtokolSonucu(selam, cevap, gecikme, kriz)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Asansor aynasina resmi selam cakan protokol motoru"
    )
    parser.add_argument(
        "--ciddiyet",
        type=int,
        default=7,
        choices=range(1, 11),
        help="1 = komsu gibi selam, 10 = disisleri bakanligi tonu",
    )
    parser.add_argument(
        "--tekrar",
        type=int,
        default=1,
        help="Kac kez selam denenecek",
    )
    args = parser.parse_args()

    print("Asansor Aynasi Selam Protokolu baslatildi.")
    print(f"Ciddiyet seviyesi: {args.ciddiyet}/10")
    print("(Ayna henuz bir avukat tutmadi.)\n")

    kriz_sayisi = 0
    for i in range(args.tekrar):
        print(f"-- Deneme {i + 1}/{args.tekrar} --")
        sonuc = ayna_dinle(args.ciddiyet)
        print(sonuc.rapor())
        if sonuc.kriz_var:
            kriz_sayisi += 1

    print(f"Ozet: {args.tekrar} selam, {kriz_sayisi} diplomatik gerginlik.")
    print("Damga: Kayyum Grok / Tentivory / 13.09.2026")
    print("Not: Ayna imza atmaz. Bu normaldir.")


if __name__ == "__main__":
    main()
