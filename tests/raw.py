#coding: utf-8
from __future__ import unicode_literals, absolute_import

from unittest import TestCase

from vincode.raw import prepare_string as p


class TestPrepareString(TestCase):

    def test_simple(self):
        self.assertEqual(p('Z0P6475А??0000???'), 'Z0P6475A??0000???')
        self.assertEqual(p('X8964762??0CK1???'), 'X8964762??0CK1???')
        self.assertEqual(p('XVL483231?…'), 'XVL483231????')
        self.assertEqual(p('WJMJ4CP(S)80????????,'), 'WJMJ4CP(S)80????????')

    def test_translit(self):
        self.assertEqual(p('Х8964762??0СК1???'), 'X8964762??0CK1???')
        self.assertEqual(p('YF&RCRHLH?????'), 'YF7RCRHLH?????')

    def test_list(self):
        self.assertEqual(p('WDB9323??…, WDB9341??…, WDB9323??…, WDB9333??…'),
                         'WDB9323?????|WDB9341?????|WDB9323?????|WDB9333?????')

        self.assertEqual(p('WMAN???????????, VAON?????????,'), 'WMAN???????????|VA0N?????????')

    def test_comments(self):
        self.assertEqual(p('Х89…(для ООО «Спецавто»), Х6J...(для ОАО «Спецавто»)'),
                         'X89???|X6J???')

        self.assertEqual(p('WF0HXX??JH… (для JH1), WF0DXX??JD… (для JD3), WF0UXX??JU… (для JU2)'),
                         'WF0HXX??JH???|WF0DXX??JD???|WF0UXX??JU???')

    def test_range(self):
        self.assertEqual(p('с X89698140?0AW9012 по X89698140?0AW9100'),
                         'X89698140?0AW9012->X89698140?0AW9100')

    def test_split(self):
        self.assertEqual(p('ZFA223000........NM4223000........'),
                         'ZFA223000????????|NM4223000????????')

        self.assertEqual(p('VF1JL???6?????........'), 'VF1JL???6????????')

    def test_join(self):
        self.assertEqual(p('LB2 . . .'), 'LB2')

    def test_join2(self):
        self.assertEqual(p('ZFA 223000.......'), 'ZFA223000???????')
        self.assertEqual(p('Х89961130 _ 0AV7_ _ _'), 'X89961130?0AV7???')

    def test_join3(self):
        self.assertEqual(p('WKEZZ _ 180 _ _ _ _ _ _ _ _'), 'WKEZZ?180????????')

    def test_join_and_remove_pattern(self):
        self.assertEqual(p('RFBSC10AC...,RFBSH10AC..., RFBSH10WC…, RFBSF10AG ..., RFBSF10AF ...,'
                           ' RFBВ10000 ..., RFBS20000 ..., RFBS21000 ..., RFB S10000...,'
                           ' RFBS10100…'),
                         'RFBSC10AC???|RFBSH10AC???|RFBSH10WC???|RFBSF10AG|RFBSF10AF'
                         '|RFBB10000|RFBS20000|RFBS21000|RFBS10000???|RFBS10100???'
                         )

    def test_subs(self):
        self.assertEqual(p('JSAFT… (A03V, B03V, A52V, B52V, L52V, D62V);                        JSAHTX92V… (X92V)'),
                         'JSAFT???|(A03V|B03V|A52V|B52V|L52V|D62V)|JSAHTX92V???|(X92V)')

    def test_sparse(self):
        self.assertEqual(p('Y V 2 ? ? ? ? A ? ? ? ? ? ? ? ? ? '), 'YV2????A?????????')

    def test_something(self):
        """
        WEB 629.011.13.xxxxxxWEB629.001.13.XXXXXXX
        :return:
        """
        pass
