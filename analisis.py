from neo4j import GraphDatabase
import matplotlib.pyplot as plt
import pandas as pd


class analyst(object):
    neo_connection = None

    def __init__(self, neo_driver):
        self.neo_connection = neo_driver.session()

    def partido_presupuesto_licitaciones(self):
        query_par = "match  (Par:Partido)-[r:Gobierna]->(ccaa:CCAA)-[a:Asigna]->(adj:Adjudicatario)" \
                    "WHERE toInteger(a.importe_adjudicacion) <> 0 " \
                    "return Par.name, sum(toInteger(a.presupuesto)), " \
                    "sum(toInteger(a.valor_estimado)),sum(toInteger(a.importe_adjudicacion))"
        grafica_partido_presupuesto_lic(self.neo_connection.run(query_par).data())

        # return self.neo_connection.run(query_par).data()

    def ccaa_presupuesto_licitaciones(self):
        query_par = "match  (Par:Partido)-[r:Gobierna]->(ccaa:CCAA)-[a:Asigna]->(adj:Adjudicatario)" \
                    "WHERE toInteger(a.importe_adjudicacion) <> 0 " \
                    "return ccaa.name,sum(toInteger(a.presupuesto)), " \
                    "sum(toInteger(a.valor_estimado)),sum(toInteger(a.importe_adjudicacion))"
        grafica_ccaa_presupuesto_lic(self.neo_connection.run(query_par).data())
        # return self.neo_connection.run(query_par).data()

    def afiliado_presupuesto_licitaciones(self):
        query_par = "match  (Par:Partido)-[r:Gobierna]->(ccaa:CCAA)-[a:Asigna]->(adj:Adjudicatario)" \
                    "WHERE toInteger(a.importe_adjudicacion) <> 0 " \
                    "and  toInteger(r.desde) <= toInteger(a.anio) <= toInteger(r.hasta) " \
                    " return r.afiliado,  sum(toInteger(a.presupuesto)), " \
                    "sum(toInteger(a.valor_estimado)),sum(toInteger(a.importe_adjudicacion))" \
                    " order by sum(toInteger(a.presupuesto))desc limit 17"
        grafica_afiliado_presupuesto_lic(self.neo_connection.run(query_par).data())
        # return self.neo_connection.run(query_par).data()

    def anio_licitaciones(self):
        query_par = "match (Par:Partido)-[r:Gobierna]->(ccaa:CCAA)-[a:Asigna]->(adj:Adjudicatario)" \
                    " return a.anio, count(*) order by a.anio desc limit 4"
        grafica_anio_licitaciones(self.neo_connection.run(query_par).data())

    def licitaciones_partido(self):
        query_par = "match (Par:Partido)-[r:Gobierna]->(ccaa:CCAA)-[a:Asigna]->(adj:Adjudicatario)" \
                    " return Par.name, count(*)"
        grafica_lic_partido(self.neo_connection.run(query_par).data())
        # return self.neo_connection.run(query_par).data()

    def afiliado_licitaciones(self):
        query_par = "match  (Par:Partido)-[r:Gobierna]->(ccaa:CCAA)-[a:Asigna]->(adj:Adjudicatario) " \
                    "return r.afiliado, count(*) order by count(*) desc limit 17"
        grafica_lic_afiliado(self.neo_connection.run(query_par).data())
        # return self.neo_connection.run(query_par).data()

    def ccaa_licitaciones(self):
        query_par = "match  (Par:Partido)-[r:Gobierna]->(ccaa:CCAA)-[a:Asigna]->(adj:Adjudicatario) " \
                    "return ccaa.name, count(*)"
        grafica_lic_ccaa(self.neo_connection.run(query_par).data())
        # return self.neo_connection.run(query_par).data()

    def ccaa_licitaciones_2020_2021(self):
        query_ccaa_2020 = "match  (Par:Partido)-[r:Gobierna]->(ccaa:CCAA)-[a:Asigna]->(adj:Adjudicatario) " \
                          "WHERE  toInteger(r.desde) <= 2020 <= toInteger(r.hasta) " \
                          "and toInteger(a.anio) = 2020 return ccaa.name, count(*) order by ccaa.name"
        # self.neo_connection.run(query_ccaa).data()

        query_afi_2020 = "match  (Par:Partido)-[r:Gobierna]->(ccaa:CCAA)-[a:Asigna]->(adj:Adjudicatario) " \
                         "WHERE  toInteger(r.desde) <= 2020 <= toInteger(r.hasta) " \
                         "and toInteger(a.anio) = 2020 return r.afiliado, count(*) order by r.afiliado"
        # self.neo_connection.run(query_par).data()
        query_par_2020 = "match  (Par:Partido)-[r:Gobierna]->(ccaa:CCAA)-[a:Asigna]->(adj:Adjudicatario) " \
                         "WHERE  toInteger(r.desde) <= 2020 <= toInteger(r.hasta) " \
                         "and toInteger(a.anio) = 2020 return Par.name, count(*) order by Par.name"
        # self.neo_connection.run(query_par_2021).data()

        query_ccaa_2021 = "match  (Par:Partido)-[r:Gobierna]->(ccaa:CCAA)-[a:Asigna]->(adj:Adjudicatario) " \
                          "WHERE  toInteger(r.desde) <= 2021 <= toInteger(r.hasta) " \
                          "and toInteger(a.anio) = 2021 return ccaa.name, count(*) order by ccaa.name"
        # self.neo_connection.run(query_ccaa).data()

        query_afi_2021 = "match  (Par:Partido)-[r:Gobierna]->(ccaa:CCAA)-[a:Asigna]->(adj:Adjudicatario) " \
                         "WHERE  toInteger(r.desde) <= 2021 <= toInteger(r.hasta) " \
                         "and toInteger(a.anio) = 2021 return r.afiliado, count(*) order by r.afiliado"
        # self.neo_connection.run(query_afi_2021).data()
        query_par_2021 = "match  (Par:Partido)-[r:Gobierna]->(ccaa:CCAA)-[a:Asigna]->(adj:Adjudicatario) " \
                         "WHERE  toInteger(r.desde) <= 2021 <= toInteger(r.hasta) " \
                         "and toInteger(a.anio) = 2021 return Par.name, count(*) order by Par.name"
        # self.neo_connection.run(query_par_2021).data()

        grafica_ccaa_licitaciones_2020_2021(self.neo_connection.run(query_ccaa_2020).data(),
                                            self.neo_connection.run(query_ccaa_2021).data())
        grafica_afiliado_licitaciones_2020_2021(self.neo_connection.run(query_afi_2020).data(),
                                                self.neo_connection.run(query_afi_2021).data())

        grafica_partido_licitaciones_2020_2021(self.neo_connection.run(query_par_2020).data(),
                                               self.neo_connection.run(query_par_2021).data())

    def partido_presupuesto_licitaciones_2020_2021(self):
        query_par_2020 = "match  (Par:Partido)-[r:Gobierna]->(ccaa:CCAA)-[a:Asigna]->(adj:Adjudicatario)" \
                         "WHERE toInteger(a.importe_adjudicacion) <> 0 and toInteger(r.desde) <= 2020 <= toInteger(r.hasta) " \
                         "and toInteger(a.anio) = 2020 return Par.name, sum(toInteger(a.presupuesto)), " \
                         "sum(toInteger(a.valor_estimado)),sum(toInteger(a.importe_adjudicacion))" \
                         " order by sum(toInteger(a.presupuesto)), sum(toInteger(a.importe_adjudicacion)) desc limit 17"

        query_par_2021 = "match  (Par:Partido)-[r:Gobierna]->(ccaa:CCAA)-[a:Asigna]->(adj:Adjudicatario)" \
                         "WHERE toInteger(a.importe_adjudicacion) <> 0 and toInteger(r.desde) <= 2021 <= toInteger(r.hasta) " \
                         "and toInteger(a.anio) = 2021 return Par.name, sum(toInteger(a.presupuesto)), " \
                         "sum(toInteger(a.valor_estimado)),sum(toInteger(a.importe_adjudicacion))" \
                         " order by sum(toInteger(a.presupuesto)), sum(toInteger(a.importe_adjudicacion)) desc limit 17"
        grafica_partido_presupuesto_licitaciones_2020_2021(self.neo_connection.run(query_par_2020).data(),
                                                           self.neo_connection.run(query_par_2021).data())

    def ccaa_presupuesto_licitaciones_2020_2021(self):
        query_ccaa_2022 = "match  (Par:Partido)-[r:Gobierna]->(ccaa:CCAA)-[a:Asigna]->(adj:Adjudicatario)" \
                          "WHERE toInteger(a.importe_adjudicacion) <> 0 and toInteger(r.desde) <= 2022 <= toInteger(r.hasta) " \
                          "and toInteger(a.anio) = 2022 return ccaa.name, sum(toInteger(a.presupuesto)), " \
                          "sum(toInteger(a.valor_estimado)),sum(toInteger(a.importe_adjudicacion))" \
                          " order by ccaa.name"

        query_ccaa_2021 = "match  (Par:Partido)-[r:Gobierna]->(ccaa:CCAA)-[a:Asigna]->(adj:Adjudicatario)" \
                          "WHERE toInteger(a.importe_adjudicacion) <> 0 and toInteger(r.desde) <= 2021 <= toInteger(r.hasta) " \
                          "and toInteger(a.anio) = 2021 return ccaa.name, sum(toInteger(a.presupuesto)), " \
                          "sum(toInteger(a.valor_estimado)),sum(toInteger(a.importe_adjudicacion))" \
                          " order by ccaa.name"
        grafica_ccaa_presupuesto_licitaciones_2020_2021(self.neo_connection.run(query_ccaa_2022).data(),
                                                        self.neo_connection.run(query_ccaa_2021).data())

    def pnv_adjudicatarios(self):
        # columna de ccaa, columna si es importe o presupuesto y valor
        # madrid, presupuesto, 213321
        # madrid, importe, 1233214
        # seaborn group por 2 col
        # HISTOGRAMA PARA PNV escala log por el valor de adjudicacion O HISTOGRAMA DENTOR DE HISTOGRAMA
        # y grafo
        # explicar los de restringido publico
        query_count = "MATCH (n:Partido{name:'PNV'})-[r:Gobierna]->(ccaa:CCAA)-[a:Asigna]->(adj:Adjudicatario)" \
                      " where toInteger(r.desde) <= 2022 <= toInteger(r.hasta) and toInteger(a.anio) = 2022  " \
                      "RETURN adj.name, count(*),sum(toInteger(a.presupuesto)), sum(toInteger(a.importe_adjudicacion)) " \
                      "order by count(*) desc"

        query_presupuestos = "MATCH (n:Partido{name:'PNV'})-[r:Gobierna]->(ccaa:CCAA)-[a:Asigna]->(adj:Adjudicatario) " \
                             "where toInteger(r.desde) <= 2022 <= toInteger(r.hasta)and toInteger(a.anio) = 2022 " \
                             " AND toInteger(a.presupuesto) <2000 RETURN adj.name,toInteger(a.presupuesto), " \
                             "toInteger(a.importe_adjudicacion) order by adj.name"

        grafica_pnv(self.neo_connection.run(query_count).data(), self.neo_connection.run(query_presupuestos).data())

    def publico_adj(self):
        query_par = "match  (Par:Partido)-[r:Gobierna]->(ccaa:CCAA)-[a:Asigna]->(adj:Adjudicatario)" \
                    " where adj.name = 'Restringido/Publico'  return ccaa.name, count(*) order by ccaa.name desc"
        # query_par_data = self.neo_connection.run(query_par).data()
        query_par_total = "match  (Par:Partido)-[r:Gobierna]->(ccaa:CCAA)-[a:Asigna]->(adj:Adjudicatario)" \
                          "where ccaa.name <> 'Melilla' return ccaa.name, count(*) order by ccaa.name desc"
        grafica_adj_pub_ccaa(self.neo_connection.run(query_par).data(), self.neo_connection.run(query_par_total).data())

    def publico_adj_par(self):
        query_par = "match  (Par:Partido)-[r:Gobierna]->(ccaa:CCAA)-[a:Asigna]->(adj:Adjudicatario)" \
                    " where adj.name = 'Restringido/Publico'  return Par.name, count(*) order by Par.name desc"
        # query_par_data = self.neo_connection.run(query_par).data()
        query_par_total = "match  (Par:Partido)-[r:Gobierna]->(ccaa:CCAA)-[a:Asigna]->(adj:Adjudicatario)" \
                          "where ccaa.name <> 'Melilla' return Par.name, count(*) order by Par.name desc"
        grafica_publico_adj_par(self.neo_connection.run(query_par).data(), self.neo_connection.run(query_par_total).data())

    def boxplot_intercualtil(self):
        query_ccaa = "match  (Par:Partido)-[r:Gobierna]->(ccaa:CCAA)-[a:Asigna]->(adj:Adjudicatario)" \
                    "WHERE toInteger(a.importe_adjudicacion) <> 0 " \
                    "return ccaa.name, sum(toInteger(a.presupuesto)), " \
                    "sum(toInteger(a.importe_adjudicacion))"

        query_par = "match  (Par:Partido)-[r:Gobierna]->(ccaa:CCAA)-[a:Asigna]->(adj:Adjudicatario)" \
                    "WHERE toInteger(a.importe_adjudicacion) <> 0 " \
                    "return Par.name, sum(toInteger(a.presupuesto)), " \
                    "sum(toInteger(a.importe_adjudicacion))"

        query_afi = "match  (Par:Partido)-[r:Gobierna]->(ccaa:CCAA)-[a:Asigna]->(adj:Adjudicatario)" \
                    "WHERE toInteger(a.importe_adjudicacion) <> 0 " \
                    "and  toInteger(r.desde) <= toInteger(a.anio) <= toInteger(r.hasta) " \
                    " return r.afiliado,  sum(toInteger(a.presupuesto)), " \
                    "sum(toInteger(a.valor_estimado)),sum(toInteger(a.importe_adjudicacion))" \
                    " order by sum(toInteger(a.presupuesto))desc limit 17"
        grafica_intercuartil_ccaa(self.neo_connection.run(query_ccaa).data())
        grafica_intercuartil_ccaa(self.neo_connection.run(query_par).data())
        grafica_intercuartil_ccaa(self.neo_connection.run(query_afi).data())

def grafica_intercuartil_ccaa(lista_dict):
    print(lista_dict)
    nombre_ccaa = []
    presupuesto = []
    importe_adjudicacion = []
    ratio = []

    for x in range(0, len(lista_dict)):
        # nombre_ccaa.append(lista_dict[x]['ccaa.name'])
        presupuesto.append(lista_dict[x]['sum(toInteger(a.presupuesto))']/1000000)
        importe_adjudicacion.append(lista_dict[x]['sum(toInteger(a.importe_adjudicacion))']/1000000)

    data = [presupuesto, importe_adjudicacion]

    # plt.figure(figsize=(10, 7))

    # Creating axes instance
    # ax = fig.add_axes([0, 0, 1, 1])

    # Creating plot
    # plt.boxplot(data)

    # show plot
    # plt.show()


    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111)

    # Creating axes instance
    bp = ax.boxplot(data, patch_artist=True,
                    notch='True', vert=0)

    colors = ['#0000FF', '#00FF00',
              '#FFFF00', '#FF00FF']

    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)

    # changing color and linewidth of
    # whiskers
    # for whisker in bp['whiskers']:
    #     whisker.set(color='#8B008B',
    #                 linewidth=1.5,
    #                 linestyle=":")

    # changing color and linewidth of
    # caps
    # for cap in bp['caps']:
        # cap.set(color='#8B008B',
        #         linewidth=2)

    # changing color and linewidth of
    # medians
    for median in bp['medians']:
        median.set(color='red',
                   linewidth=3)

    # changing style of fliers
    # for flier in bp['fliers']:
    #     flier.set(marker='D',
    #               color='#e7298a',
    #               alpha=0.5)

    # x-axis labels
    ax.set_yticklabels(['Presupuesto', 'Importe de adjudicacion'])

    # Adding title
    plt.title("Posibles outlayers")

    # Removing top axes and right axes
    # ticks
    # ax.get_xaxis().tick_bottom()
    # ax.get_yaxis().tick_left()

    # show plot
    plt.show()

def grafica_publico_adj_par(count_restringido, count_total):
    nombre_partido = []
    restringido = []
    total = []
    ratio = []
    # print(len(count_restringido))
    # print(len(count_total))
    # print(count_restringido)
    # print(count_total)

    for x in range(0, len(count_restringido)):
        nombre_partido.append(count_restringido[x]['Par.name'])
        restringido.append(count_restringido[x]['count(*)'])
        total.append(count_total[x]['count(*)'])
        ratio.append(((count_restringido[x]['count(*)']) * 100) / (
                count_total[x]['count(*)']))
    df = pd.DataFrame(list(zip(nombre_partido, restringido, total)),
                      columns=["Partido", "Restringidos", "Total"])
    # df.plot.bar(figsize=(15, 5), secondary_y='Presupuesto(Millones)', x="Comunidad Autonoma")
    df.plot.bar(figsize=(15, 5), x="Partido")
    plt.savefig("./img/par_restringido_adjudicacion.png")
    plt.show()

    plt.plot(nombre_partido, ratio, color='red', marker='o')
    plt.title('Ratio CCAA', fontsize=14)
    plt.xlabel('CCAA', fontsize=14)
    plt.ylabel('Ratio(%)', fontsize=14)
    plt.xticks(rotation=90)
    plt.grid(True)
    plt.savefig("./partido_restringido_adjudicacion_RATIO.png")
    plt.show()

def grafica_adj_pub_ccaa(count_restringido, count_total):
    nombre_ccaa = []
    restringido = []
    total = []
    ratio = []
    print(count_restringido)
    print(count_total)
    # print(count_total)

    for x in range(0, len(count_restringido)):
        nombre_ccaa.append(count_restringido[x]['ccaa.name'])
        restringido.append(count_restringido[x]['count(*)'])
        total.append(count_total[x]['count(*)'])
        ratio.append(((count_restringido[x]['count(*)']) * 100) / (
                count_total[x]['count(*)']))
    df = pd.DataFrame(list(zip(nombre_ccaa, restringido, total)),
                      columns=["Comunidad Autonoma", "Restringidos", "Total"])
    # df.plot.bar(figsize=(15, 5), secondary_y='Presupuesto(Millones)', x="Comunidad Autonoma")
    df.plot.bar(figsize=(15, 5), x="Comunidad Autonoma")
    plt.savefig("./img/ccaa_restringido_adjudicacion.png")
    plt.show()

    plt.plot(nombre_ccaa, ratio, color='red', marker='o')
    plt.title('Ratio CCAA', fontsize=14)
    plt.xlabel('CCAA', fontsize=14)
    plt.ylabel('Ratio(%)', fontsize=14)
    plt.xticks(rotation=90)
    plt.grid(True)
    plt.savefig("./ccaa_restringido_adjudicacion_RATIO.png")
    plt.show()

def grafica_pnv(count_result, presupuestos_result):
    #print(count_result)
    new_count_result = []
    new_count_result_adj = []
    new_pre_result_adj = []
    new_pre_result_presupuesto = []
    for x in range(0, len(count_result)):
        if int(count_result[x]['count(*)']) > 1:
            new_count_result_adj.append(count_result[x]['adj.name'])
            new_count_result.append(int(count_result[x]['count(*)']))

    for x in range(0, len(presupuestos_result)):
        if presupuestos_result[x]['adj.name'] in new_count_result_adj:
            new_pre_result_adj.append(presupuestos_result[x]['adj.name'])
            new_pre_result_presupuesto.append(presupuestos_result[x]['toInteger(a.presupuesto)'])
    #print(new_count_result_adj)
    #print(new_count_result_adj)
    #print(new_pre_result_adj)
   # print(new_pre_result_presupuesto)
    import seaborn as sns

    df = pd.DataFrame(list(zip(new_pre_result_adj, new_pre_result_presupuesto)),
                      columns=["Adjudicatario", "Presupuesto"])

    df.hist(figsize=(15, 5))
    plt.savefig("./img/presupuesto_repetido.png")
    plt.show()

    df = pd.DataFrame(list(zip(new_count_result_adj, new_count_result)),
                      columns=["Adjudicatario", "Presupuesto"])

    df.plot.bar(figsize=(15, 5), x='Adjudicatario')
    plt.savefig("./img/count_adj.png")
    plt.show()


def grafica_ccaa_presupuesto_licitaciones_2020_2021(lista_dict_2022, lista_dict_2021):
    nombre_ccaa = []
    presupuesto = []
    importe_adjudicacion = []
    resta_2022 = []
    resta_2021 = []
    print(lista_dict_2022)
    # print(lista_dict_2021)
    print("-----------------------------------")
    for x in range(0, len(lista_dict_2021)):
        print(lista_dict_2021[x]['ccaa.name'])
        nombre_ccaa.append(lista_dict_2021[x]['ccaa.name'])
        resta_2021.append((lista_dict_2021[x]['sum(toInteger(a.presupuesto))'] -
                           lista_dict_2021[x]['sum(toInteger(a.importe_adjudicacion))']) / 1000)
        # presupuesto.append(lista_dict_2020[x]['sum(toInteger(a.presupuesto))']/1000000)
        # importe_adjudicacion.append(lista_dict_2020[x]['sum(toInteger(a.importe_adjudicacion))']/1000000)
    print("-----------------------------------")

    for x in range(0, len(lista_dict_2022)):


        # nombre_partidos.append(lista_dict_2020[x]['Par.name'])
        if lista_dict_2022[x]['ccaa.name'] in nombre_ccaa:
            print(lista_dict_2022[x]['ccaa.name'])
            resta_2022.append((lista_dict_2022[x]['sum(toInteger(a.presupuesto))'] -
                               lista_dict_2022[x]['sum(toInteger(a.importe_adjudicacion))']) / 1000)

    print(nombre_ccaa)
    print(resta_2022)
    print(resta_2021)
    df = pd.DataFrame(list(zip(nombre_ccaa, resta_2022, resta_2021)),
                      columns=["Comunidad Autonoma", "Presupuesto - Importe Adjudicacion 2022 (Miles)",
                               "Presupuesto - Importe Adjudicacion 2021 (Miles)"])
    df.plot.bar(figsize=(15, 5), x="Comunidad Autonoma")
    plt.savefig("./img/ccaa_presupuesto_2022-2021.png")
    plt.show()


def grafica_partido_presupuesto_licitaciones_2020_2021(lista_dict_2020, lista_dict_2021):
    nombre_partidos = []
    presupuesto = []
    importe_adjudicacion = []
    resta_2020 = []
    resta_2021 = []

    for x in range(0, len(lista_dict_2020)):
        nombre_partidos.append(lista_dict_2020[x]['Par.name'])
        resta_2020.append((lista_dict_2020[x]['sum(toInteger(a.presupuesto))'] -
                           lista_dict_2020[x]['sum(toInteger(a.importe_adjudicacion))']) / 1000000)
        # presupuesto.append(lista_dict_2020[x]['sum(toInteger(a.presupuesto))']/1000000)
        # importe_adjudicacion.append(lista_dict_2020[x]['sum(toInteger(a.importe_adjudicacion))']/1000000)
    for x in range(0, len(lista_dict_2021)):
        # nombre_partidos.append(lista_dict_2020[x]['Par.name'])
        if lista_dict_2021[x]['Par.name'] in nombre_partidos:
            resta_2021.append((lista_dict_2021[x]['sum(toInteger(a.presupuesto))'] -
                               lista_dict_2021[x]['sum(toInteger(a.importe_adjudicacion))']) / 1000000)

    print(nombre_partidos)
    print(resta_2020)
    print(resta_2021)
    df = pd.DataFrame(list(zip(nombre_partidos, resta_2020, resta_2021)),
                      columns=["Partido", "Presupuesto - Importe Adjudicacion 2020 (Millones)",
                               "Presupuesto - Importe Adjudicacion 2021 (Millones)"])
    df.plot.bar(figsize=(15, 5), secondary_y='Presupuesto - Importe Adjudicacion 2021 (Millones)', x="Partido")
    plt.savefig("./img/partido_presupuesto_2020-2021.png")
    plt.show()


def grafica_partido_presupuesto_lic(lista_dict):
    nombre_partidos = []
    presupuesto = []
    importe_adjudicacion = []
    ratio = []

    for x in range(0, len(lista_dict)):
        nombre_partidos.append(lista_dict[x]['Par.name'])
        presupuesto.append(lista_dict[x]['sum(toInteger(a.presupuesto))'] / 1000000)
        importe_adjudicacion.append(lista_dict[x]['sum(toInteger(a.importe_adjudicacion))'] / 1000000)
        # resta = (lista_dict[x]['sum(toInteger(a.presupuesto))'] / 1000000) - (lista_dict[x]['sum(toInteger(a.importe_adjudicacion))'] / 1000000))
        ratio.append(100-(((lista_dict[x]['sum(toInteger(a.importe_adjudicacion))'] / 1000000) * 100)/(lista_dict[x]['sum(toInteger(a.presupuesto))'] / 1000000)))
    # df = pd.DataFrame(list(zip(nombre_partidos, presupuesto, importe_adjudicacion)),
    #                   columns=["Partido", "Presupuesto(Millones)", "Importe Adjudicacion(Millones)"])
    # # df.plot.bar(figsize=(15, 5), secondary_y='Presupuesto(Millones)', x="Partido")
    # df.plot.bar(figsize=(15, 5), x="Partido")
    # plt.savefig("./img/partido_presupuesto_importe_adjudicacion.png")
    # plt.show()

    plt.plot(nombre_partidos, ratio, color='red', marker='o')
    plt.title('Ratio partido', fontsize=14)
    plt.xlabel('Partido', fontsize=14)
    plt.ylabel('Ratio(%)', fontsize=14)
    plt.xticks(rotation=90)
    plt.grid(True)
    plt.savefig("./img/partido_presupuesto_importe_adjudicacion_RATIO.png")
    plt.show()


def grafica_afiliado_presupuesto_lic(lista_dict):
    afiliado = []
    presupuesto = []
    importe_adjudicacion = []
    cont = 0
    ratio = []
    print(lista_dict)

    for x in range(0, len(lista_dict)):
        afiliado.append(lista_dict[x]['r.afiliado'])
        presupuesto.append((lista_dict[x]['sum(toInteger(a.presupuesto))'] / 1000000 ))
        importe_adjudicacion.append((lista_dict[x]['sum(toInteger(a.importe_adjudicacion))'] / 1000000))
        cont += 1
        ratio.append(100 - (((lista_dict[x]['sum(toInteger(a.importe_adjudicacion))'] / 1000000) * 100) / ((
                lista_dict[x]['sum(toInteger(a.presupuesto))'] / 1000000))))
    df = pd.DataFrame(list(zip(afiliado, presupuesto, importe_adjudicacion)),
                      columns=["Afiliado", "Presupuesto(Millones)", "Importe Adjudicacion(Millones)"])
    print(afiliado)
    # df.plot.bar(figsize=(15, 5), secondary_y='Presupuesto(Millones)', x="Afiliado")
    df.plot.bar(figsize=(15, 5), x="Afiliado")
    plt.savefig("./img/afiliado_presupuesto_importe_adjudicacion.png")
    plt.show()

    plt.plot(afiliado, ratio, color='red', marker='o')
    plt.title('Ratio Afiliado', fontsize=14)
    plt.xlabel('Afiliado', fontsize=14)
    plt.ylabel('Ratio(%)', fontsize=14)
    plt.xticks(rotation=90)
    plt.grid(True)
    plt.savefig("./img/afiliado_presupuesto_importe_adjudicacion_RATIO.png")
    plt.show()


def grafica_ccaa_presupuesto_lic(lista_dict):
    nombre_ccaa = []
    presupuesto = []
    importe_adjudicacion = []
    ratio = []

    for x in range(0, len(lista_dict)):
        nombre_ccaa.append(lista_dict[x]['ccaa.name'])
        presupuesto.append(lista_dict[x]['sum(toInteger(a.presupuesto))'] / 1000000)
        importe_adjudicacion.append(lista_dict[x]['sum(toInteger(a.importe_adjudicacion))'] / 1000000)
        ratio.append(100 - (((lista_dict[x]['sum(toInteger(a.importe_adjudicacion))'] / 1000000) * 100) / (
            lista_dict[x]['sum(toInteger(a.presupuesto))'] / 1000000)))
    df = pd.DataFrame(list(zip(nombre_ccaa, presupuesto, importe_adjudicacion)),
                      columns=["Comunidad Autonoma", "Presupuesto(Millones)", "Importe Adjudicacion(Millones)"])
    # df.plot.bar(figsize=(15, 5), secondary_y='Presupuesto(Millones)', x="Comunidad Autonoma")
    df.plot.bar(figsize=(15, 5), x="Comunidad Autonoma")
    plt.savefig("./img/ccaa_presupuesto_importe_adjudicacion.png")
    plt.show()

    plt.plot(nombre_ccaa, ratio, color='red', marker='o')
    plt.title('Ratio CCAA', fontsize=14)
    plt.xlabel('CCAA', fontsize=14)
    plt.ylabel('Ratio(%)', fontsize=14)
    plt.xticks(rotation=90)
    plt.grid(True)
    plt.savefig("./img/ccaa_presupuesto_importe_adjudicacion_RATIO.png")
    plt.show()


def grafica_lic_partido(lista_dict):
    nombre_partidos = []
    num_lic = []
    for x in range(0, len(lista_dict)):
        nombre_partidos.append(lista_dict[x]['Par.name'])
        num_lic.append(lista_dict[x]['count(*)'])
    print(nombre_partidos)
    print(num_lic)
    plt.bar(nombre_partidos, num_lic)
    plt.ylabel("Numbero de Licitaciones")
    plt.xlabel("Partidos/Coaliciones")
    plt.title("Licitaciones aprobadas por partidos")
    # plt.grid()

    plt.gca().margins(x=0)
    plt.gcf().canvas.draw()
    tl = plt.gca().get_xticklabels()
    maxsize = max([t.get_window_extent().width for t in tl])
    m = 0.2  # inch margin
    s = maxsize / plt.gcf().dpi * 150 + 2 * m
    margin = m / plt.gcf().get_size_inches()[0]

    plt.gcf().subplots_adjust(left=margin, right=1. - margin)
    plt.gcf().set_size_inches(s, plt.gcf().get_size_inches()[1])
    plt.savefig("./img/partido_licitaciones.png")
    plt.show()

def grafica_anio_licitaciones(lista_dict):
    nombre_anio = []
    num_lic = []
    for x in range(0, len(lista_dict)):
        nombre_anio.append(lista_dict[x]['a.anio'])
        num_lic.append(lista_dict[x]['count(*)'])
    print(nombre_anio)
    print(num_lic)
    plt.bar(nombre_anio, num_lic)
    plt.ylabel("Numero de Licitaciones")
    plt.xlabel("Años")
    plt.title("Licitaciones aprobadas por año")
    # plt.grid()

    plt.gca().margins(x=0)
    plt.gcf().canvas.draw()
    tl = plt.gca().get_xticklabels()
    maxsize = max([t.get_window_extent().width for t in tl])
    m = 0.2  # inch margin
    s = maxsize / plt.gcf().dpi * 150 + 2 * m
    margin = m / plt.gcf().get_size_inches()[0]

    plt.gcf().subplots_adjust(left=margin, right=1. - margin)
    plt.gcf().set_size_inches(s, plt.gcf().get_size_inches()[1])
    plt.savefig("./img/anio_licitaciones.png")
    plt.show()


def grafica_lic_ccaa(lista_dict):
    nombre_ccaa = []
    num_lic = []
    for x in range(0, len(lista_dict)):
        # fix para el titulo del eje
        if lista_dict[x]['ccaa.name'] == 'Principado de Asturias':
            nombre_ccaa.append('Prin. Asturias')
        elif lista_dict[x]['ccaa.name'] == 'Comunidad de Madrid':
            nombre_ccaa.append('Com. Madrid')
        elif lista_dict[x]['ccaa.name'] == 'Comunidad Valenciana':
            nombre_ccaa.append('Com. Valenciana')
        elif lista_dict[x]['ccaa.name'] == 'Región de Murcia':
            nombre_ccaa.append('Reg. Murcia')
        else:
            nombre_ccaa.append(lista_dict[x]['ccaa.name'])
        num_lic.append(lista_dict[x]['count(*)'])
    print(nombre_ccaa)
    print(num_lic)
    plt.bar(nombre_ccaa, num_lic)
    plt.ylabel("Numbero de Licitaciones")
    plt.xlabel("Comunidad Autonoma")
    plt.title("Licitaciones aprobadas por Comunidades Autonomas")
    # plt.grid()

    plt.gca().margins(x=0)
    plt.gcf().canvas.draw()
    tl = plt.gca().get_xticklabels()
    maxsize = max([t.get_window_extent().width for t in tl])
    m = 0.2  # inch margin
    s = maxsize / plt.gcf().dpi * 200 + 2 * m
    margin = m / plt.gcf().get_size_inches()[0]

    plt.gcf().subplots_adjust(left=margin, right=1. - margin)
    plt.gcf().set_size_inches(s, plt.gcf().get_size_inches()[1])
    plt.savefig("./img/ccaa_licitaciones.png")

    plt.show()


def grafica_lic_afiliado(lista_dict):
    nombre_afiliado = []
    num_lic = []
    for x in range(0, len(lista_dict)):
        nombre_afiliado.append(str(lista_dict[x]['r.afiliado']).replace(" ", "\n"))
        num_lic.append(lista_dict[x]['count(*)'])
    print(nombre_afiliado)
    print(num_lic)
    plt.bar(nombre_afiliado, num_lic)
    plt.ylabel("Numbero de Licitaciones")
    plt.xlabel("Afiliado")
    plt.title("Licitaciones aprobadas por afiliados")
    # plt.grid()

    plt.gca().margins(x=0)
    plt.gcf().canvas.draw()
    tl = plt.gca().get_xticklabels()
    maxsize = max([t.get_window_extent().width for t in tl])
    m = 0.2  # inch margin
    s = maxsize / plt.gcf().dpi * 150 + 2 * m
    margin = m / plt.gcf().get_size_inches()[0]

    plt.gcf().subplots_adjust(left=margin, right=1. - margin)
    plt.gcf().set_size_inches(s, plt.gcf().get_size_inches()[1])
    plt.savefig("./img/afiliado_licitaciones.png")

    plt.show()


def grafica_ccaa_licitaciones_2020_2021(lista_dict_2020, lista_dict_2021):
    # print(lista_dict_2020)
    # print(lista_dict_2021)
    # print("-------------------------------------")
    nombre_ccaa_2020 = []
    nombre_ccaa_2021 = []
    num_lic2020 = []
    num_lic2021 = []
    for x in range(0, len(lista_dict_2020)):
        nombre_ccaa_2020.append(str(lista_dict_2020[x]['ccaa.name']).replace(" ", "\n"))
        num_lic2020.append(lista_dict_2020[x]['count(*)'])
    for x in range(0, len(lista_dict_2021)):
        if str(lista_dict_2021[x]['ccaa.name'].replace(" ", "\n")) in nombre_ccaa_2020:
            nombre_ccaa_2021.append(str(lista_dict_2021[x]['ccaa.name']).replace(" ", "\n"))
            num_lic2021.append(lista_dict_2021[x]['count(*)'])

    df = pd.DataFrame(list(zip(nombre_ccaa_2020, num_lic2020, num_lic2021)),
                      columns=["Comunidad Autonoma", "Numero Licitaciones 2020", "Numero Licitaciones 2021"])
    df.plot.bar(figsize=(15, 5), secondary_y='Numero Licitaciones 2021', x="Comunidad Autonoma")
    plt.savefig("./img/ccaa_licitaciones_2020-21.png")

    plt.show()
    # print(nombre_ccaa_2020)
    # print(num_lic2020)
    # print(nombre_ccaa_2021)
    # print(num_lic2021)
    # plt.bar(nombre_afiliado, num_lic)
    # plt.ylabel("Numbero de Licitaciones")
    # plt.xlabel("Afiliado")
    # plt.title("Licitaciones aprobadas por afiliados")
    # # plt.grid()
    #
    # plt.gca().margins(x=0)
    # plt.gcf().canvas.draw()
    # tl = plt.gca().get_xticklabels()
    # maxsize = max([t.get_window_extent().width for t in tl])
    # m = 0.2  # inch margin
    # s = maxsize / plt.gcf().dpi * 150 + 2 * m
    # margin = m / plt.gcf().get_size_inches()[0]
    #
    # plt.gcf().subplots_adjust(left=margin, right=1. - margin)
    # plt.gcf().set_size_inches(s, plt.gcf().get_size_inches()[1])
    # plt.show()


def grafica_afiliado_licitaciones_2020_2021(lista_dict_2020, lista_dict_2021):
    # print(lista_dict_2020)
    # print(lista_dict_2021)
    # print("-------------------------------------")
    nombre_afiliado_2020 = []
    nombre_afiliado_2021 = []
    num_lic2020 = []
    num_lic2021 = []
    for x in range(0, len(lista_dict_2020)):
        nombre_afiliado_2020.append(str(lista_dict_2020[x]['r.afiliado']).replace(" ", "\n"))
        num_lic2020.append(lista_dict_2020[x]['count(*)'])
    for x in range(0, len(lista_dict_2021)):
        if str(lista_dict_2021[x]['r.afiliado'].replace(" ", "\n")) in nombre_afiliado_2020:
            nombre_afiliado_2021.append(str(lista_dict_2021[x]['r.afiliado']).replace(" ", "\n"))
            num_lic2021.append(lista_dict_2021[x]['count(*)'])

    df = pd.DataFrame(list(zip(nombre_afiliado_2020, num_lic2020, num_lic2021)),
                      columns=["Afiliado", "Numero Licitaciones 2020", "Numero Licitaciones 2021"])
    df.plot.bar(figsize=(15, 5), secondary_y='Numero Licitaciones 2021', x="Afiliado")
    plt.savefig("./img/afiliado_licitaciones_2020-21.png")

    plt.show()
    # print(nombre_afiliado_2020)
    # print(num_lic2020)
    # print(nombre_afiliado_2021)
    # print(num_lic2021)


def grafica_partido_licitaciones_2020_2021(lista_dict_2020, lista_dict_2021):
    # print(lista_dict_2020)
    # print(lista_dict_2021)
    # print("-------------------------------------")
    nombre_partido_2020 = []
    nombre_partido_2021 = []
    num_lic2020 = []
    num_lic2021 = []
    for x in range(0, len(lista_dict_2020)):
        nombre_partido_2020.append(str(lista_dict_2020[x]['Par.name']).replace(" ", "\n"))
        num_lic2020.append(lista_dict_2020[x]['count(*)'])
    for x in range(0, len(lista_dict_2021)):
        if str(lista_dict_2021[x]['Par.name'].replace(" ", "\n")) in nombre_partido_2020:
            nombre_partido_2021.append(str(lista_dict_2021[x]['Par.name']).replace(" ", "\n"))
            num_lic2021.append(lista_dict_2021[x]['count(*)'])

    df = pd.DataFrame(list(zip(nombre_partido_2020, num_lic2020, num_lic2021)),
                      columns=["Partido", "Numero Licitaciones 2020", "Numero Licitaciones 2021"])

    df.plot.bar(figsize=(15, 5), secondary_y='Numero Licitaciones 2021', x="Partido")
    plt.savefig("./img/partido_licitaciones_2020-21.png")

    plt.show()


class BDDD_Conection(object):
    neo_connection = None

    def __init__(self, neo_driver):
        self.neo_connection = neo_driver.session()


neo_driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "1234"))
BDDD_Conection(neo_driver)
analyst = analyst(neo_driver)
# TODO: PARA ENTENDER LOS DATOS
# analyst.licitaciones_partido()
# analyst.ccaa_licitaciones()
# analyst.afiliado_licitaciones()
# analyst.anio_licitaciones()
# TODO: FIXED
# analyst.partido_presupuesto_licitaciones()
# analyst.afiliado_presupuesto_licitaciones()
# analyst.ccaa_presupuesto_licitaciones()
# TODO: PNV
# analyst.pnv_adjudicatarios()
# TODO: TODAVIA NO HAY DATOS
# analyst.ccaa_licitaciones_2020_2021()
# analyst.partido_presupuesto_licitaciones_2020_2021()
# analyst.ccaa_presupuesto_licitaciones_2020_2021()
# TODO: EXTRA DE PUBLICO
# analyst.publico_adj()
# analyst.publico_adj_par()
# TODO: BOXPLOT
analyst.boxplot_intercualtil()
# partido_presupuesto_lic        = analyst.partido_presupuesto_licitaciones()
# afiliado_presupuesto_lic         = analyst.afiliado_presupuesto_licitaciones()
# ccaa_presupuesto_lic             = analyst.ccaa_presupuesto_licitaciones()
# lic_partido                    = analyst.licitaciones_partido()
# ccaa_lic                       = analyst.ccaa_licitaciones()
# afiliado_lic                   = analyst.afiliado_licitaciones()
# ccaa_lic_2020, afiliado_lic_2020l, ccaa_lic_2021, afiliado_lic_2021  = analyst.ccaa_licitaciones_2020_2021()
# ccaa_lic_2021, afiliado_lic_2021 = analyst.ccaa_licitaciones_2021()
# -------------------------------------------------------------------
# grafica_partido_presupuesto_lic(partido_presupuesto_lic)
# grafica_afiliado_presupuesto_lic(afiliado_presupuesto_lic)
# grafica_ccaa_presupuesto_lic(ccaa_presupuesto_lic)
# grafica_lic_partido(lic_partido)
# grafica_lic_ccaa(ccaa_lic)
# grafica_lic_afiliado(afiliado_lic)
print("FIN")
