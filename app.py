from flask import Flask, render_template, jsonify, url_for
import json

app = Flask(__name__)

# Carregar os processos do arquivo JSON
with open('processos.json', 'r', encoding='utf-8') as f:
    processos = json.load(f)

@app.route('/')
def index():
    areas = list(processos.keys())
    return render_template('index.html', areas=areas)

@app.route('/cargos/<area>')
def get_cargos(area):
    cargos = list(processos[area].keys())
    return jsonify(cargos)

@app.route('/processos/<area>/<cargo>')
def get_processos(area, cargo):
    processo_list = list(processos[area][cargo].keys())
    return jsonify(processo_list)

@app.route('/detalhes/<area>/<cargo>/<processo>')
def get_detalhes(area, cargo, processo):
    detalhes = processos[area][cargo][processo]
    return jsonify(detalhes)

@app.route('/fluxograma/<area>/<cargo>/<processo>')
def get_fluxograma(area, cargo, processo):
    # Mapear os processos para as URLs das imagens dos fluxogramas
    fluxogramas = {
        "Setor Financeiro": {
            "Supervisor Financeiro": {
                "Solicitação de Ativação do Cartão Zona Azul": url_for('static', filename='Doc. SolicitaÃ§Ã£o de AtivaÃ§Ã£o do CartÃ£o Zona Azul (2) 27.07.2023 - Luigi Ximenes.png'),
                "Revisão das Provisões de Pagamento": url_for('static', filename='Doc. RevisÃ£o das ProvisÃµes de Pagamento (3) 30.08.2023 - Luigi Ximenes.png'),
                "Recebimento de Notas Fiscais Físicas": url_for('static', filename='Doc. Recebimento De Notas Fiscais FÃ­sicas (3) 29.08.2023 - Luigi Ximenes.png'),
                "Recebimento de Notas Fiscais - Digital": url_for('static', filename='Doc. Recebimento De Notas Fiscais Digitais (2) 18.08.2023 - Luigi Ximenes.png'),
                "Realização de Pagamentos": url_for('static', filename='Doc. RealizaÃ§Ã£o De Pagamentos (3) 11.08.2023 - Luigi Ximenes.png'),
                "Pagamento Luz": url_for('static', filename='Doc. Pagamento De Luz (3) 21.08.2023 - Luigi Ximenes.png'),
                "Pagamento de Alimentação Após Horário": url_for('static', filename='Doc. Pagamento De AlimentaÃ§Ã£o ApÃ³s o HorÃ¡rio (3) 18.08.2023 - Luigi Ximenes.png'),
                "Pagamento Água": url_for('static', filename='Doc. Pagamento De Ãgua (2) 17.08.2023 - Luigi Ximenes.png'),
                "OS de Resgate de Equipamento": url_for('static', filename='Doc. OS De Resgate De Equipamento (1) 20.07.2023- Luigi XImenes.png'),
                "OS de Reclamação de Fatura (PIX)": url_for('static', filename='Doc. OS de ReclamaÃ§Ã£o de fatura PIX (1) 25.07.2023 - Luigi Ximenes.png'),
                "Conferência de Recebimentos de PIX em Andamento": url_for('static', filename='Doc. ConferÃªncia De Recebimentos De Pix em Andamento (2) 25.08.2023 - Luigi Ximenes.png'),
                "Conciliações Bancárias": url_for('static', filename='Doc. ConciliaÃ§Ãµes BancÃ¡rias (2) 30.08.2023 - Luigi Ximenes.png'),
                "Atualização dos Valores da Folha de Pagamento (Passagem e Alimentação)": url_for('static', filename='Doc. AtualizaÃ§Ã£o Dos Valores Da Passagem e AlimentaÃ§Ã£o Da Folha De Pagamento (3) 29.08.2023 - Luigi Ximenes.png'),
                "Atualização dos Valores da Folha de Pagamento (Quinzena e Folha de Pagamento)": url_for('static', filename='Doc. AtualizaÃ§Ã£o Dos Valores Da Folha De Pagamento (3) 30.08.2023 - Luigi Ximenes.png'),
                "Atualização do Sistema OMIE": url_for('static', filename='Doc. AtualizaÃ§Ã£o Do Sistema OMIE (3) 11.08.2023 - Luigi Ximenes.png'),
                "Atualização da Provisão de Pagamento da Alimentação dos Funcionários": url_for('static', filename='Doc. AtualizaÃ§Ã£o Da ProvisÃ£o de Pagamento Da AlimentaÃ§Ã£o dos FuncionÃ¡rios (3) 29.08.2023 - Luigi Ximenes.png'),
                "Atualização da Planilha de Comissão Referente ao Pagamento das Escolas": url_for('static', filename='Doc. AtualizaÃ§Ã£o Da Planilha De ComissÃ£o Referente Ao Pagamento  Das Escolas (3) 29.08.2023.png'),
                "Arquivamento de Documentos Físicos": url_for('static', filename='Doc. Arquivamento De Documentos FÃ­sicos (3) 18.08.2023 - Luigi Ximenens.png'),
                "Arquivamento de Documentos Digitais": url_for('static', filename='Doc. Arquivamento De Documentos Digitais (3) 18.08.2023 - Luigi Ximenes.png'),
                "Arquivamento de Comprovantes": url_for('static', filename='Doc. Arquivamento De Comprovantes (2) 27.07.2023 - Luigi Ximenes.png'),
                "Adição de Funcionário no Plano de Saúde": url_for('static', filename='Doc. AdiÃ§Ã£o De FuncionÃ¡rio No Plano de SaÃºde (4) 15.08.2023 - Luigi Ximenes.png'),
                "Acompanhamento de Compras no Cartão Corporativo": url_for('static', filename='Doc. Acompanhamento De Compras No CartÃ£o Corporativo (2) 28.08.2023 - Luigi Ximenes.png'),
                "Consulta e Negativação no Serasa": url_for('static', filename='Doc. Consulta e NegativaÃ§Ã£o no Serasa (2) 08.08.2023 - Luigi Ximenes.png'),
                "Consulta dos Devedores no Serasa": url_for('static', filename='Doc. Consulta Dos Devedores No Serasa (2) 15.08.2023 - Luigi Ximenes.png'),
                "Consulta das Notas Fiscais": url_for('static', filename='Doc. Consulta Das Notas Fiscais (2)17.08.2023 - Luigi Ximenes.png'),
                "Geração de Boletos dos Clientes (Escolas)": url_for('static', filename='Doc. GeraÃ§Ã£o De Boletos Dos Clientes (Escolas) (2) 24.08.2023 - Luigi XImenes.png'),
                "Fechamento Mensal": url_for('static', filename='Doc. Fechamento Mensal (2) 23.08.2023 - Luigi Ximenes.png'),
                "Extração de Relatório de Entrada e Saída": url_for('static', filename='Doc. ExtraÃ§Ã£o De RelatÃ³rio De Entrada e SaÃ­da (3) 30.08.2023 - Luigi Ximenes.png'),
                "Exclusão de Provisão": url_for('static', filename='Doc. ExclusÃ£o De ProvisÃ£o (2) 28.08.2023 - Luigi Ximenes.png'),
                "Exclusão de Pessoas no Serasa": url_for('static', filename='Doc. ExclusÃ£o De Pessoas No Serasa (2) 15.08.2023 - Luigi Ximenes.png'),
                "OS de Monitoramento de Pagamento": url_for('static', filename='Doc. OS de monitoramento de pagamento (2) 16.08.2023 - Luigi Ximenes.png'),
                "OS de Isenção de Taxa": url_for('static', filename='Doc. OS De IsenÃ§Ã£o De Taxa (2) 16.08.2023 - Luigi Ximenes.png'),
                "OS de Desvinculação do ONU": url_for('static', filename='Doc. OS De DesvinculaÃ§Ã£o do ONU (1) 20.07.2023 - Luigi Ximenes.png'),
                "OS de Cancelamento de Contrato e Título": url_for('static', filename='Doc. OS De cancelamento De contrato e TÃ­tulo (2) 16.08.2023 - Luigi Ximenes.png'),
                "OS de Cancelamento de Contrato": url_for('static', filename='Doc. OS de Cancelamento De Contrato (2) 16.08.2023 - Luigi Ximenes.png'),
                "Emissão das Notas Fiscais - Serviço": url_for('static', filename='Doc. EmissÃ£o Das Notas FIscais ServiÃ§o (3) 18.08.2023 - Luigi Ximenes.png'),
                "Confirmação de Pagamento dos Boletos das Escolas": url_for('static', filename='Doc. ConfirmaÃ§Ã£o De Pagamento Dos Boletos Das Escolas (3) 29.08.2023 - Luigi Ximenes'),
                "Geração de Boletos dos Clientes (Geral)": url_for('static', filename='Doc. GeraÃ§Ã£o De Boletos Dos Clientes (Geral) (2) 24.08.2023 - Luigi XImenes.png'),
                "Manutenção da Planilha": url_for('static', filename='Doc. ManutenÃ§Ã£o Das Planilhas (2) 15.08.2023 - Luigi XImenes.png'),
                "Lançamentos Provisões Anuais": url_for('static', filename='Doc. LanÃ§amento Das ProvisÃµes Anuais (2) 23.08.2023 - Luigi Ximenes.png'),
                "Emissão das Notas Fiscais - Vendas": url_for('static', filename='Doc. EmissÃ£o Das Notas FIscais Venda (2) 18.08.2023 - Luigi Ximenes.png'),
                "OS de Reclamação de Fatura (BOLETO NÃO EXCLUÍDO)": url_for('static', filename='Doc. OS de ReclamaÃ§Ã£o de fatura Boleto ExcluÃ­do (1) 25.07.2023 - Luigi Ximenes.png'),
                "OS de Reclamação de Fatura": url_for('static', filename='Doc. OS de ReclamaÃ§Ã£o de fatura (2) 18.08.2023 - Luigi Ximenes.png'),
                "Controle PAG": url_for('static', filename='Doc. Controle PAG (3) 23.07.2023 - Luigi Ximenes.png'),
                "OS de Cancelamento de Cobrança": url_for('static', filename='Doc. OS de cancelamento de cobranÃ§a (2) 16.08.2023 - Luigi Ximenes.png')
            }
        }
    }

    fluxograma = fluxogramas.get(area, {}).get(cargo, {}).get(processo, None)
    if fluxograma:
        return jsonify({"fluxograma": fluxograma})
    else:
        return jsonify({"fluxograma": None})

if __name__ == '__main__':
    app.run(debug=True)
