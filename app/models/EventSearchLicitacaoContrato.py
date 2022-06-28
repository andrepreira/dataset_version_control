# coding=utf-8
import collections
import re


class EventSearcher(object):

    def __init__(self):
        self.events = collections.OrderedDict([
            ('TERMO DE APOSTILAMENTO AO CONTRATO', [r'termo de apostilamento ao contrato', r'TERMO DE APOSTILAMENTO AO CONTRATO']),
            ('TERMO DE RATIFICACAO', [r'termo de ratificacao', r'RATIFICACAO DE INEXIGIBILIDADE', r'TERMO DE RATIFICACAO']),
            ('EXTRATO DE CONTRATO', [r'extrato de contrato', r'EXTRATO DO CONTRATO']),
            ('TERMO ADITIVO', [r'termo aditivo', r'EXTRATO DE TERMO ADITIVO']),
            ('EXTRATO DE DISTRATO', [r'extrato de distrato']),            
            ('EXTRATO DE DISPENSA DE LICITACAO', [r'extrato de dispensa de licitacao']),
            ('AVISO DE INEXIGIBILIDADE', [r'aviso de inexigibilidade']),            
            ('EXTRATO DE INEXIGIBILIDADE', [r'extrato de inexigibilidade', r'EXTRATO DE INEXIGIBILIDADE', r'EXTRATO CONTRATUAL INEXIGIBILIDADE']),
            ('AVISO DE LICITACAO', [r'aviso de licitacao', r'AVISO DE LICITACAO']),
            ('AVISO DE LICITACAO - PREGAO', [r'\sLICITACAO', r'PREGAO ELETRONICO', r'PREGAO']),
            ('AVISO DE LICITACAO - TOMADA DE PRECOS', [r'TOMADA DE PRECOS', r'AVISO DE LICITACAO TOMADA DE PRECOS']),
            ('RETIFICACAO DE LICITACAO', [r'retificacao de licitacao', r'RETIFICACAO DE LICITACAO', r'RETIFICACAO DO PREGAO']),
            ('AVISO DE SUSPENSAO', [r'aviso de suspensao']),
            ('AVISO DE COTACAO', [r'aviso de cotacao', r'AVISO DE COTACAO']),
            ('HOMOLOGACAO', [r'homologacao', r'HOMOLOGACAO']),
            ('ADJUDICACAO', [r'adjudicacao', r'ADJUDICACAO']),
            ('EXTRATO DE ATA DE REGISTRO DE PRECO', [r'extrato de ata de registro de preco', r'EXTRATO DE ATA DE REGISTRO DE PRECOS']),
        ])

        self.events_regex = {}

        for event in self.events.keys():
            self.events_regex[event] = []

            for regex in self.events[event]:
                regex = regex.replace(' ', r'\s*')
                self.events_regex[event].append(re.compile(regex, re.DOTALL | re.MULTILINE | re.IGNORECASE))

    def search(self, snippet):
        for event in self.events.keys():
            for keyword in self.events[event]:
                if keyword in snippet:
                    return event

            for regex in self.events_regex[event]:
                match = regex.search(snippet)
                if match is not None:
                    return event

        return None