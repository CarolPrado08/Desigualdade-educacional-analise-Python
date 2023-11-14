from fpdf import FPDF   

class PDF(FPDF):

    def doc_title(self, label):
        self.set_font('helvetica', 'B', size=16)
        self.cell(0, 10, label, 0, 1, 'L')
        self.ln(8)


    def doc_text(self, text):
        
        self.set_font('helvetica', '', size=12)
        self.multi_cell(0, 7, text)
        self.ln()


    def doc_img(self, img, x, y, w, h):
        self.image(img, x, y, h)
        

pdf = PDF()
pdf.add_page()

pdf.doc_title("RELATÓRIO DESENVOLVIDO COM PYTHON")

pdf.doc_title("Desigualdade Educacional no Brasil")

pdf.doc_text("A educação desempenha um papel fundamental na promoção da igualdade de oportunidades e no desenvolvimento de uma sociedade equitativa. No entanto, a realidade da educação no Brasil é marcada por desafios significativos, com desigualdades profundas que afetam o acesso, a qualidade e a equidade do sistema educacional no país. Este relatório tem como objetivo analisar a desigualdade educacional no Brasil por meio da análise de uma planilha com dados da educação superior no país, focando em dados-chave que destacam disparidades regionais, estruturais e socioeconômicas que impactam esse nível de educação no país.")

pdf.doc_text("A educação superior é um elemento crucial na formação de indivíduos, na promoção da mobilidade social e no desenvolvimento econômico de uma nação. No entanto, essa análise revelará que o acesso a essa etapa fundamental da educação está longe de ser uniforme no Brasil. Neste relatório, serão examinados os dados que demonstram a desigualdade regional na distribuição de universidades, a predominância de instituições privadas com fins lucrativos, o crescimento da modalidade de ensino a distância (EAD) e as implicações socioeconômicas dessa realidade educacional. ")

pdf.doc_text("Desse modo, por meio da análise desses aspectos, é possível oferecer uma breve visão das desigualdades educacionais no Brasil e destacar a urgência de medidas para promover um sistema educacional mais inclusivo e igualitário. Já que a educação é a chave para o progresso social e econômico, e abordar essas disparidades é essencial para o desenvolvimento sustentável do país.")

pdf.ln(15)

pdf.doc_title("1.1 Desigualdade regional na distribuição de universidades")


pdf.doc_text("A desigualdade regional na distribuição de universidades é, com certeza, uma das características mais marcantes do sistema educacional brasileiro. O gráfico abaixo mostra uma grande concentração das universidades no Sudeste do Brasil, que é composto pelos estados de São Paulo, Rio de Janeiro, Minas Gerais e Espírito Santo, sendo a região que concentra a maior parte significativa das universidades do país. De acordo com os dados coletados, essa região abriga uma proporção substancial de instituições de ensino superior, incluindo universidades públicas e privadas. Por exemplo, só o estado de São Paulo sozinho possui praticamente o dobro ou triplo das universidades das outras regiões.")

pdf.ln(10)

pdf.ln(95)

pdf.doc_img("Universidades-por-regiao.png", 45, 30, 110, 110)

pdf.doc_text("É visível o contraste das outras regiões do Brasil, como o Norte e o Centro-Oeste, que enfrentam uma escassez alarmante de universidades. Estes estados apresentam uma proporção muito menor de instituições de ensino superior em comparação com o Sudeste. A distância geográfica e a falta de acesso a universidades em algumas áreas rurais dessas regiões contribuem para uma disparidade regional significativa no acesso à educação superior.")

pdf.doc_text("A desigualdade regional na distribuição de universidades tem várias implicações, afetando diretamente o acesso dos estudantes à educação superior. Aqueles que residem em áreas com poucas instituições de ensino enfrentam obstáculos significativos, como a necessidade de se deslocar para regiões distantes ou mesmo a falta de opções educacionais.")

pdf.doc_text("Além disso, essa desigualdade pode levar à concentração de talentos e recursos nas regiões mais privilegiadas, resultando em um desequilíbrio no desenvolvimento econômico e social do país. A mobilidade social e as oportunidades de emprego também podem ser limitadas para os residentes de áreas sub-representadas em termos de educação superior.")


pdf.doc_title("1.2 Universidades Privadas VS Públicas")

pdf.doc_text("A predominância de universidades privadas com fins lucrativos no Brasil é um dos fatores que contribuem significativamente para a desigualdade educacional no país. De acordo com o gráfico, a grande maioria das instituições de ensino superior no Brasil opera com fins lucrativos. Essas instituições cobram mensalidades dos alunos e têm o objetivo de gerar lucro para seus acionistas ou proprietários. Essa predominância de universidades privadas com fins lucrativos é um traço distintivo dentro do sistema educacional brasileiro.")


pdf.doc_img("Privadas-vs-publicas.png", 50, 50, 100, 100)
pdf.ln(80)


pdf.doc_text("Uma das principais implicações desse cenário é a acessibilidade financeira para estudantes. As mensalidades cobradas pelas instituições de ensino privadas com fins lucrativos podem ser significativamente mais elevadas do que as de instituições públicas. Isso cria barreiras para estudantes de baixa renda, que podem encontrar dificuldades em arcar com os custos da educação superior.")



pdf.doc_img("Privadas-por-regiao.png", 10, 170, 110, 110)
pdf.doc_img("Publicas-por-regiao.png", 100, 170, 110, 110)

pdf.ln(70)


pdf.doc_text(" Além disso, a desigualdade regional também se faz presente nesses dados, já que o Norte e o Centro-Oeste detém da menor quantidade de universidade tanto públicas quanto privadas. E a predominância de universidades privadas com fins lucrativos pode acentuar a desigualdade educacional. Estudantes que não têm recursos financeiros suficientes podem ser excluídos do acesso à educação superior ou optar por cursos de qualidade inferior devido às restrições financeiras. Isso resulta em disparidades no acesso a oportunidades educacionais e, por consequência, no acesso a empregos de alta qualidade e mobilidade social.")

pdf.doc_title("1.3 Crescimento da Educação à distância")

pdf.doc_text("O crescimento da modalidade de ensino a distância (EAD) no Brasil é um fenômeno notável que tem transformado a paisagem da educação superior no país. Os dados revelam que essa modalidade se tornou amplamente prevalente no ensino superior brasileiro, representando uma parcela significativa das instituições e cursos. O número de cursos e programas oferecidos nessa modalidade tem crescido constantemente nos últimos anos, refletindo uma tendência nacional.")

pdf.ln(10)

pdf.doc_img("Modalidade-ensino.png", 70, 90, 90, 90)

pdf.ln(80)

pdf.doc_text("Segundo uma pesquisa do Censo de Educação Superior no Brasil realizado pelo INEP (Instituto Nacional de Estudos e Pesquisas), foi relatado que entre 2011 e 2021, o número de ingressantes em cursos superiores de graduação, na modalidade de educação a distância (EaD), aumentou 474%. E no mesmo período, a quantidade de ingressantes em cursos presenciais diminuiu 23,4%. Passando a porcetagem de ingressos por meio de EaD em 2011 que correspondiam a 18,4% do total, e em 2021, esse percentual chegou a 62,8%.")

pdf.doc_text("Uma das principais razões para o crescimento da EAD é a acessibilidade e a flexibilidade que ela oferece. Alunos que enfrentam desafios geográficos, como a falta de universidades em suas regiões, podem agora acessar o ensino superior por meio da educação a distância. Além disso, a flexibilidade de horários permite que pessoas que trabalham ou têm outras responsabilidades possam buscar a educação superior. O que evidencia a desigualdade de acordo o sucesso da modalidade cada vez mais crecente no país.")

pdf.doc_text("Porém, enquanto a EAD oferece benefícios significativos em termos de acessibilidade e flexibilidade, há preocupações legítimas sobre a qualidade da educação oferecida nessa modalidade. A falta de interação presencial com professores e colegas, bem como os desafios tecnológicos, podem afetar negativamente a experiência de aprendizado e a aquisição de habilidades.")

pdf.doc_text("Assim sendo, as pessoas que mais se beneficiam do EAD são aquelas que tem acesso a melhores recursos tecnológicos, melhor conexão com a internet, fazendo com que a populaçao de baixa renda tenha problemas para ter um bom proveito da modalidade. ")

pdf.doc_text("Por tanto, o crescimento da EAD tem implicações diretas na desigualdade educacional. Aqueles que têm acesso a recursos tecnológicos de alta qualidade e uma boa conexão com a internet podem se beneficiar da modalidade EAD. No entanto, a falta de acesso a esses recursos pode excluir muitos estudantes, criando uma divisão digital.")

pdf.doc_title("1.4 Predominância de cursos de grau tecnológico")

pdf.doc_text("Por fim, também foi possível observar que os de cursos de grau Tecnológico no sistema de ensino superior brasileiro são uma característica notável que merece ser analisada. Os dados coletados revelam que os cursos de grau Tecnológico são amplamente predominantes no cenário educacional brasileiro. Eles compreendem uma parcela significativa dos programas de ensino superior disponíveis, superando em número as tradicionais Licenciaturas e Bacharelados.")

pdf.doc_img("Cursos-por-grau.png", 40, 180, 120, 120)

pdf.ln(90)

pdf.doc_text("Para entender essa predominância, é importante considerar os motivos subjacentes. Uma das razões frequentemente citadas é a maior rapidez na obtenção do diploma. Os cursos de grau Tecnológico geralmente têm uma duração mais curta em comparação com Licenciaturas e Bacharelados, o que atrai estudantes que desejam ingressar mais rapidamente no mercado de trabalho.")

pdf.doc_text("Embora os cursos de grau Tecnológico ofereçam benefícios em termos de tempo e acesso ao mercado de trabalho, há preocupações legítimas sobre a qualidade da educação proporcionada. A natureza mais focada e prática desses cursos pode resultar em uma formação mais estreita, limitando a amplitude do conhecimento e das habilidades adquiridas.")

pdf.ln(80)

pdf.doc_img("Grau-por-regiao.png", 50, 80, 110, 110)

pdf.doc_text("A predominância dos cursos de grau Tecnológico tem implicações diretas na desigualdade educacional. Aqueles que optam por esses cursos podem obter diplomas mais rapidamente, mas podem enfrentar limitações em sua formação em comparação com Licenciaturas e Bacharelados. Essas limitações podem impactar suas perspectivas de carreira e mobilidade social.")

pdf.doc_title("Conclusão")

pdf.doc_text("Em conclusão, este relatório destacou a presença de desigualdades educacionais profundas no Brasil, especialmente no âmbito do ensino superior. A desigualdade regional na distribuição de universidades, a predominância de instituições de ensino privadas com fins lucrativos, o crescimento da modalidade de ensino a distância (EAD) e a predominância de cursos de grau tecnológico são alguns dos aspectos que contribuem para a disparidade no acesso à educação superior.")

pdf.doc_text("A análise demonstra que as disparidades encontradas não apenas afetam o acesso dos estudantes a oportunidades educacionais, mas também têm implicações mais amplas no desenvolvimento econômico e social do país. A mobilidade social e as oportunidades de emprego são desafiadas para aqueles que vivem em áreas sub-representadas em termos de educação superior.")

pdf.doc_text("Portanto, fica claro a necessidade de que medidas sejam tomadas para promover um sistema educacional mais inclusivo e igualitário no Brasil. A educação, como chave para o progresso social e econômico, precisa abordar essas desigualdades para o desenvolvimento sustentável do país. Assim sendo, a promoção de acesso equitativo à educação superior, a melhoria da qualidade da EAD e a consideração das implicações de longo prazo dos cursos de grau tecnológico são passos importantes na busca por uma sociedade mais justa e igualitária no Brasil.")


pdf.output("Projeto.pdf")