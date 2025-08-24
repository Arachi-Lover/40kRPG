def load_classes_data():
    classes_data = {
        "Marine Neófito": {
            "Status": {
                "Vida": 4,
                "Iniciativa": 3,
                "Armadura": 3,
                "Perícia": 1,
                "Moral": 1
            },
            "Habilidades": {
                "Conhecimento (Império)": 2,
                "Conhecimento (Caos)": 2,
                "Conhecimento (Aliens)": 1,
                "Técnico": 1,
                "Carisma": 1,
                "Percepção": 2,
                "Resistência": 2,
                "Atleticismo": 3
            },
            "Nativas": [
                "Superforça - Permite interagir com objetos de tamanho/massa enorme",
                "Mesmo na morte - Quando este personagem chega a 0 de vida, imediatamente inicia um último turno",
                "Anjos do Imperador - Uma vez por batalha, quando um ataque reduziria os pontos de vida de outro membro da party a 0, o Marine pode receber o dano em seu lugar"
            ],
            "Combate": {
                "Ações": 3,
                "Habilidades": [
                    "Fogo Concentrado (2 ações): Acerto 3+, Dano 1, Alvos 1 - Role 2 dados. Se o resultado em ambos for o mesmo cause 1 de dano adicional ao inimigo",
                    "Disparar à Vontade (2 ações): Acerto 4+, Dano 1, Alvos 3",
                    "Disparo Singular (1 ação): Acerto 5+, Dano 1, Alvos 1",
                    "Espada-serra (1 ação) [Ataque Corporal]: Acerto 4+, Dano 1, Alvos 1"
                ]
            },
            "Customização": {
                "Gênero": "Apenas Masculino",
                "Opções de Nativa Bônus": [
                    "Escudo Inquebrável - Até o Marine receber dano pela primeira vez na batalha, sua Armadura é tratada como valor 4",
                    "Uma Última Lâmina - Uma vez por batalha, se ao final de suas ações de combate o Marine não tiver conseguido eliminar o último alvo de seus ataques, e esse alvo tiver apenas 1 de Vida restante, o alvo é apunhalado pelo Marine e morre"
                ],
                "Triunfos": [
                    "Orgulho da XIII - Sua proeza em combate e habilidade nata para a logística da guerra, paerada com sua inabalável adaptabilidade em meio ao combate, fez com que o Sargento responsável por sua unidade o parabenizasse, elogiando-o como um verdadeiro filho do primarca Roboute Guilliman. Desde então, você ganhou ainda mais motivação para ser digno desse elogio, e se empenha cada vez mais para exercer sua função com excelência.",
                    "Protetor de Ultramar - Durante uma sequência de treinamento, o planeta em que estava foi invadido pelos extragaláticos Tyranids. O campo de batalha cobriu o planeta, mas durante todo o tempo você conseguiu defender, acalmar e resguardar uma família de civis inocentes dos predadores ferozes. Quando os reforços chegaram pare lhe resgatar, e a paz retornou ao planeta, você foi reconhecido como uma espécie de celebridade local, e ganhou um talento e certo gosto por ajudar mortais em situações difíceis como essa.",
                    "Líder Nato - Você se destacou em sequências de treinamento por apresentar uma mente mais apta que o normal, mesmo entre os Marines, para táticas de combate e planejamento de guerra. Você tem facilidade para liderar, e muitas vezes é para você que os outros olham ao buscarem por um líder."
                ],
                "Vergonhas": [
                    "O Pior dos Melhores - Suas habilidades em combate facilmente superavam aquelas de qualquer homem comum, mas mesmo assim seus resultados ficaram meramente aceitáveis para o pelotão de recrutas sobrenaturalmente talentosos, e você foi o último Aspirante aceito para receber seus novos orgãos, ao ascender ao ranque de Neófito. Desde então, você não pôde deixar de se comparar aos seus colegas, e sentir-se incerto quanto à sua capacidade para o serviço.",
                    "Votos Amaldiçoados - Você nunca conseguiu dizer adeus à um hábito mortal, seja o apego à sua família, bebida, mulheres, ou algum aspecto cultural de seu planeta natal. Assim, seus superiores frequentemente o puniram por não manter-se aos votos e juramentos de um Marine, dada sua dificuldade de controlar seus impulsos.",
                    "Cirurgia Traumática - O processo para lhe conceder seus novos órgãos de Marine foi caótico. Seu corpo apresentou feroz resistência aos órgãos, reconhecendo-os como estranhos e combatendo sua inserção. Como resultado, sua cirurgia se extendeu por dias, e embora agora esteja com todos os órgãos em harmonia e funcionando, sua mente ainda tem cicatrizes e traumas do procedimento."
                ]
            },
            "img": "https://wh40k.lexicanum.com/mediawiki/images/d/df/TacticalMarine7th.jpg",
            "width": 350,
            "height": 445,
        },
        "Aprendiz do Culto Mechanicus": {
            "Status": {
                "Vida": 3,
                "Iniciativa": 2,
                "Armadura": 2,
                "Perícia": 1,
                "Moral": 2
            },
            "Habilidades": {
                "Conhecimento (Império)": 2,
                "Conhecimento (Caos)": 1,
                "Conhecimento (Aliens)": 3,
                "Técnico": 3,
                "Carisma": 2,
                "Percepção": 3,
                "Resistência": 1,
                "Atleticismo": 1
            },
            "Nativas": [
                "Eco do Canto de Marte - Permite ao aprendiz interagir com máquinário complexo",
                "Reparos - Uma vez por batalha, durante seu turno, permite restaurar 1 de Vida para: Marine, Aprendiz, ou Irmã",
                "Ritos do Omnissiah - Permite re-rolar testes Técnicos ou de Reparo (limite de 1 vez por teste)",
                "Simulação de combate - Revela a iniciativa de todos os inimigos",
                "Invasão Noosférica - Permite tentativas de hackear unidades inimigas robóticas (não alienígenas), por teste Técnico e de Perícia 12+, uma vez por batalha por unidade. Unidades hackeadas tornam-se aliadas, mas devem passar testes de moral em todos seus turnos, iniciando com 3+ e incrementando por 1 a cada turno. Caso falhe um teste de moral, a unidade volta ao lado inimigo",
                "Escudo pessoal - Uma vez por abatalha, ao ser declarado como alvo de qualquer ataque, antes de rolar o dado de Armadura, o Aprendiz pode acionar seu escudo, evitando o ataque"
            ],
            "Combate": {
                "Ações": 2,
                "Habilidades": [
                    "Desintegrador de Matéria (2 ações): Acerto 4+, Dano 1, Alvos 1 - Se o rolamento de Armadura superar em 2x ou mais a Armadura do alvo, cause 1 de dano adicional",
                    "Machado de Marte (1 ação) [Ataque Corporal]: Acerto 3+, Dano 1, Alvos 1",
                    "Fortificar, Recalibrar, Aprimorar (2 ações): O Aprendiz dispara ordens de combate por seus componentes, reforçando sua armadura com mais 1 ponto até o início de seu segundo turno após este"
                ]
            },
            "Customização": {
                "Gênero": "Masculino/Feminino",
                "Opções de Nativa Bônus": [
                    "Injeção de Adrenalina - Ao chegar a 0 de Vida, o Aprendiz recuperará 2 pontos de Vida. O Aprendiz se torna inelegível para qualquer tipo de cura, e ao final de cada um de seus próximos turnos perde 1 de Vida",
                    "Sobrecarregar Circuitos - Ao atacar, após o dado de Acerto mas antes do dado de Armadura, o Aprendiz pode gastar 1 de Vida para fortalecer o golpe, dobrando seu dano. A Vida é gasta mesmo se o dado de Armadura falhar"
                ],
                "Triunfos": [
                    "Tocado pelo Dragão - Você possui quase que um sexto sentido para o entendimento de tecnologia. Simplesmente olhar uma peça de equipamento completamente nova lhe permite formar exemplos de esquemáticas e modelagens de seu funcionamento em seus núcleos cogitativos, quase sempre acertando de primeira ao por em prática suas teorias. Você é considerado abençoado por entre os membros do Culto Mechanicus.",
                    "Vislumbre do Omnissiah - Em seu primeiro ano como Aprendiz, teve a oportunidade única de trabalhar nos reparos em uma das sagradas Máquinas-Deus, um Titã Senhor-da-Guerra, ídolo metálico do Deus Máquina. Sua experiência o deixou profundamente fixado e decidido sobre a invencibilidade das maravilhas tecnológicas da antiga humanidade, e assim você passou a encontrar suas tarefas de desvendar segredos tecnológicos comparativamente simples, imaginando o potencial humano para criar tamanho poder.",
                    "Prestígio Vermelho - Você nasceu e foi criado em solo marciano, sendo de uma família relativamente bem sucedida no coração do Culto Mechanicus, e já até pôde ver o Fabricador General de Marte em pessoa em uma grande celebração em sua juventude. Dado seu histórico, você desfruta de um status considerável entre seus colegas."
                ],
                "Vergonhas": [
                    "Perda Inestimável - Você tomou parte em uma expedição na qual a frota Mechanicus que buscava um fragmento de STC foi atacada por forças alienígenas logo após a extração do artefato sagrado. Embora não tenha sido diretamente sua culpa, o artefato foi destruído, e com ele milênios de conhecimento esquecido, e assim nasceu um estigma sobre a presença de você e dos demais magos presentes na frota derrotada ser um sinal de má sorte entre membros do Mechanicus.",
                    "Drive Corrompido - Durante uma batalha, uma bala perdida encontrou seu caminho até um de seus armazens de memória de longo prazo, estilhaçado boa parte dos arquivos lá. Felizmente, quase a totalidade de seus conhecimentos técnicos não foi afetada, mas os back-ups de suas lembranças pessoais, de sua vida antes de seus implantes mais invasivos, foram perdidos, restando-lhe apenas pequenos fragmentos nebulosos e vagos.",
                    "Código Sucateado - Em meio a uma viagem turbulenta pelo Mar de Almas, a nave em que você estava sofreu uma falha, o campo Gellar foi comprometido, e seres demoníacos abordaram a nave. Como uma praga, um dos seres alvejou todos os membros do Culto Mechanicus abordo, injetando código sem sentido, incompreensível, e incompilável, porém ao mesmo tempo intoxicante e poderoso, nos circuitos de todos. Após a expulsão dos demônios, e retorno ao espaço real, você e seus colegas sobreviventes foram purificados, mas ainda restam traços do código maldoso em você, traços que o atrapalham a discernir a realidade como ela é, por vezes, e que não lhe concedem paz em seu período offline."
                ]
            },
            "img": "https://wh40k.lexicanum.com/mediawiki/images/thumb/1/1d/TP10th.jpg/600px-TP10th.jpg",
            "width": 300,
            "height": 450,
        },

        "Irmã de Batalha": {
            "Status": {
                "Vida": 4,
                "Iniciativa": 3,
                "Armadura": 2,
                "Perícia": 1,
                "Moral": 3
            },
            "Habilidades": {
                "Conhecimento (Império)": 2,
                "Conhecimento (Caos)": 2,
                "Conhecimento (Aliens)": 2,
                "Técnico": 2,
                "Carisma": 3,
                "Percepção": 1,
                "Resistência": 2,
                "Atleticismo": 3
            },
            "Nativas": [
                "Voz Inquisitorial - Permite questionar a fé de outros personagens para tentar persuadir ou manipular uma situação",
                "Zelo - Automaticamente passa o primeiro teste de moral da batalha",
                "Hinos e Salmos - Uma vez por batalha, no início de seu turno, a Irmã aumenta a Moral de todos os membros da party por 1, até o início de seu próximo turno",
                "O Imperador protege - Quando um aliado com menos da metade da vida é selecionado como alvo de um ataque, a Irmã pode disparar contra o atacante. Teste de perícia e moral combinado 11+: caso passe, o inimigo perde 1 de vida, caso falhe a Irmã perde 1 de vida",
                "Milagre - Quando a Irmã possuir apenas 1 de vida restante, role 5 dados. Se nenhum resultado for 1, cure 2 de vida da Irmã"
            ],
            "Combate": {
                "Ações": 3,
                "Habilidades": [
                    "Medicina Sagrada (3 ações): Cura 2 de vida do alvo",
                    "Disparar à Vontade (2 ações): Acerto 3+, Dano 1, Alvos 3",
                    "Disparo Singular (1 ação): Acerto 5+, Dano 1, Alvos 1",
                    "Faca de Combate (1 ação) [Ataque Corporal]: Acerto 4+, Dano 1, Alvos 1"
                ]
            },
            "Customização": {
                "Gênero": "Apenas Feminino",
                "Opções de Nativa Bônus": [
                    "Nossas Preces Foram Atendidas! - Quando a party tiver menos da metade da Vida total coletiva, a Irmã pode escolher ceder seu turno para rolar 3 dados milagrosos. Se os 3 dados tiverem o mesmo resultado, um novo aliado se juntará à batalha imediatamente, seu primeiro turno iniciando logo após esta ação. Após o sucesso, esta Nativa não pode mais ser utilizada na mesma batalha",
                    "Extermínio - A irmã recebe um bônus de 1 de Perícia em todos os testes contra aliens, hereges, e forças do Caos"
                ],
                "Triunfos": [
                    "Intervenção - Você fez parte do batalhão em combate em um mundo onde a Santa Viva Celestine se manifestou, expulsando as legiões de demônios e liberando o mundo. Abençoada pela experiência, você tem memórias vívidas daquele dia, e pode recontar os acontecimentos fielmente, trazendo conforto para todos aqueles que seguem o Credo Imperial.",
                    "Inspiração Transcendente - Sua fé lhe concedeu tamanha ferocidade e proeza em batalha que mesmo membros dos Marines foram inspirados, impressionados por sua devoção. Os anjos do Imperador, apesar de não compartilharem, de modo geral, do Credo Imperial, passaram a ver suas ações como feitos de grandeza, mesmo assim.",
                    "Médica de Batalha - Ganhou reconhecimento por sua atuação corajosa ao tratar dos feridos e salvar vidas de tropas normalmente consideradas perdidas em meio a conflitos. Sua presença ajuda a acalmar os nervos daqueles que temem o risco de morte na guerra contra os inimigos do Império."
                ],
                "Vergonhas": [
                    "Momento de Fraqueza - Após uma batalha horrível, enquanto você examinava as ruínas, destroços, e pilhas de cadáveres mutilados e corrompidos, por alguns instantes você questionou se o Imperador havia abandonado seu Império e seu povo. Sua mente logo a corrigiu e a castigou pelos pensamentos hereges, e até hoje você possui certa paranoia quanto à sua própria fé, por vezes tendo crises internas.",
                    "Temeridade Excessiva - Sua fé excedeu suas habilidades em meio a um cerco crucial, e em suas ordens para investir contra os inimigos resultaram em quase um batalhão inteiro de Guardas ser tornado em pó por poderes além de sua compreensão. Desde então, ao contrário do padrão para os discursos inspiradores das Irmãs, suas tentativas de aumentar a moral e ferocidade de tropas com cantos sobre o Imperador trazem, na verdade, sussurros de mal agouros.",
                    "Sussurros Sombrios - Você foi enganada por um Demônio poderoso que estava se passando pelo Imperador, alimentando sua mente com mensagens subliminares em meio à supostas respostas às suas orações. Quando a Inquisição descobriu e finalmente baniu a criatura, você ainda assim continuou atormentada, e com dificuldades de confiar em qualquer outro que supostamente está seguindo a vontade do Imperador."
                ]
            },
            "img": "https://wh40k.lexicanum.com/mediawiki/images/c/c5/Red-and-black-cover-clean.jpg",
            "width": 315,
            "height": 450,
        },

        "Assassino Culexus": {
            "Status": {
                "Vida": 3,
                "Iniciativa": 5,
                "Armadura": 1,
                "Perícia": 2,
                "Moral": 1
            },
            "Habilidades": {
                "Conhecimento (Império)": 3,
                "Conhecimento (Caos)": 1,
                "Conhecimento (Aliens)": 2,
                "Técnico": 1,
                "Carisma": 1,
                "Percepção": 3,
                "Resistência": 3,
                "Atleticismo": 3
            },
            "Nativas": [
                "Aura de Morte - Permite tentativas de intimidação",
                "O Alvo - No início da batalha, um inimigo é indicado como alvo do assassino. Caso o assassino mate esse inimigo durante seu primeiro turno, todos os outros inimigos fazem um teste de moral 3+",
                "Psico-Nulo - O assassino possui +3 de armadura contra ataques psíquicos, +2 de perícia contra inimigos psíquicos, e reduz a armadura de inimigos psíquicos em -1",
                "Medo do Desconhecido - Uma vez por batalha, ao fim de seu turno, se o assassino matou um inimigo durante seu turno, ele se tornará inelegível para ataques até o início de seu próximo turno"
            ],
            "Combate": {
                "Ações": 3,
                "Habilidades": [
                    "Animus Speculum (3 ações): Acerto 5+, Dano 3, Alvos 1 - Após causar dano, caso o alvo não esteja morto, imediatamente deve fazer um teste de Moral 3+",
                    "Pistola de Executor (1 ação): Acerto 4+, Dano 1, Alvos 1",
                    "Toque Desalmado (2 ações) [Ataque Corporal]: Acerto 4+, Dano 2, Alvos 1 - Após causar dano, caso o alvo não esteja morto, imediatamente deve fazer um teste de Moral 3+"
                ]
            },
            "Customização": {
                "Gênero": "Masculino/Feminino",
                "Opções de Nativa Bônus": [
                    "Legado de M'Shen - O Assassino tem 1 Ação a mais em batalhas contra Chefes",
                    "Indetectável - O Assassino é inelegível como alvo para o primeiro ataque da batalha de cada inimigo"
                ],
                "Triunfos": [
                    "Fantasma - Auxiliando Marines em um combate contra uma a Legião Negra, você adentrou sorrateiramente na nave comandante das forças inimigas, e cortou a cabeça do senhor da guerra resposável pela campanha, sem que ninguém soubesse que você havia passado pela nave. Como parte do sigilo de seu trabalho poucos sabem de seu feito, mas sua experiência em infiltração não precisa do reconhecimento deles.",
                    "Alvos Diversos - A Inquisição conta você como um de seus assassinos favoritos, tendo utilizado seus serviços para tratar de vários alvos, como lordes Necrons, corsários e feiticeiros Eldar, e hereges e traidores de todos os tipos. Você pode não ter todas as informações sobre as atividades de seus alvos, mas sabe as melhores formas de matá-los.",
                    "Diplomata Armado - Enviado como guarda-costas para um oficial encarregado de integrar uma antiga colônia humana ao Império, foi você que se destacou como hábil negociador dos termos do acordo, conseguindo evitar um confronto e obtendo sucesso. Você também possui habilidades de persuasão e pode convencer pessoas com mais do que sua letalidade nata."
                ],
                "Vergonhas": [
                    "Caçador se Torna Caça - Em uma missão particularmente delicada, você foi descoberto por seu alvo antes de poder completá-la. Ele virou o jogo contra você, lançando uma caçada implacável que só terminou com a intervenção da Inquisição. Agora, você vive com o peso da vergonha de ter sido momentaneamente superado.",
                    "Deixado para Trás - Durante uma missão conjunta com um esquadrão de Marines, a unidade deles teve que recuar às pressas, e você foi deixado para trás. Passou semanas sobrevivendo sozinho, sabendo que seus aliados haviam seguido em frente sem você. Essa memória assombra seus sonhos e sua confiança em trabalho em equipe.",
                    "Prodígio Prepotente - Suas habilidades são de destaque mesmo entre os demais assassinos, mas sua facilidade em executar suas tarefas logo fez com que obtivesse um ego grande demais para suas funções. Pensando ter seu alvo na palma de sua mão, brincou com ele ao invés de agir rapidamente, e assim um mundo rebelde com grandes tecnologias conseguiu tempo suficiente para reforçar a posição de seu governante, gerando um fracasso para sua missão. Ainda assombrado pela falha, agora você se sente inclinado a atacar mesmo antes de analisar bem situações."
                ]
            },
            "img": "https://wh40k.lexicanum.com/mediawiki/images/f/f4/Kord.jpg",
            "width": 250,
            "height": 450,
        },

        "Psyker Sancionado": {
            "Status": {
                "Vida": 3,
                "Iniciativa": 2,
                "Armadura": 1,
                "Perícia": 2,
                "Moral": 2
            },
            "Habilidades": {
                "Conhecimento (Império)": 2,
                "Conhecimento (Caos)": 3,
                "Conhecimento (Aliens)": 2,
                "Técnico": 1,
                "Carisma": 1,
                "Percepção": 3,
                "Resistência": 2,
                "Atleticismo": 1
            },
            "Nativas": [
                "Terceiro Olho - Permite ao Psyker tentar ler mentes",
                "Forças do Além - No início de seu primeiro turno, o Psyker pode incrementar 2 de seus atributos de Status, aumentando 1 ponto em cada atributo selecionado pelo resto da batalha",
                "Possessão - Uma vez por batalha, o Psyker pode tentar sabotar um turno inimigo, fazendo um teste de Moral e de Conhecimento específico da facção do alvo 12+. Se conseguir, o Psyker controlará o inimigo durante o turno, e durante o turno o inimigo é tratado como estando aliado à party. Alvos robóticos não são válidos para Possessão"
            ],
            "Combate": {
                "Ações": 2,
                "Habilidades": [
                    "Escudo do Aether (2 ações): Alvos 1/Todos - O Psyker escolhe criar um escudo poderoso ao redor de 1 membro da party, ou de todos. Se o alvo for 1 único membro, o mesmo recebe +3 de Armadura pelos próximos 2 turnos do Psyker. Se a party inteira for o alvo, cada membro recebe +1 de Armadura pelos próximos 2 turnos do Psyker. Apenas um escudo pode estar ativo por vez",
                    "Tempestade de Raios (2 ações): Acerto 4+, Dano 1, Alvos 4",
                    "Fogo do Vazio (1 ação): Acerto 6+, Dano 2, Alvos 1",
                    "Terror do Mar de Almas (2 ações): Acerto 6+, Dano 3, Alvos 1 - Após o dano, o Psyker deve fazer um teste de Moral 5+",
                    "Baralho do Destino (2 ações): O Psyker concentra-se e vê o futuro próximo, revelando as ações do próximo turno de cada inimigo",
                    "Cajado (1 ação) [Ataque Corporal]: Acerto 4+, Dano 1, Alvos 1"
                ]
            },
            "Customização": {
                "Gênero": "Masculino/Feminino",
                "Opções de Nativa Bônus": [
                    "Manto de Ilusões - Uma vez por batalha, no início de seu turno, o Psyker pode invocar o Manto de Ilusões, subtraindo 1 dos dados de Acerto de todos os inimigos até o início de seu próximo turno",
                    "Conhecimento Proibido - No início da Batalha, o Psyker deve selecionar um inimigo. Até o fim da batalha ou até o Psyker chegar a 0 de Vida, todos os ataques desse inimigo causarão -1 de dano aos aliados do Psyker, até um mínimo de 1 de Dano por ataque (o Psyker ainda receberá o dano total, se atacado)"
                ],
                "Triunfos": [
                    "Herói Infernal - Você participou de uma campanha bem sucedida para livrar um mundo infestado pelas legiões do Caos, seus poderes psíquicos sendo cruciais para banir os demônios e retornar o mundo à normalidade. Sua presença em planetas é tida como um elemento de proteção.",
                    "Visões do Destino - Possuindo um talento especial para desvendar o futuro com seus poderes, você conseguiu evitar uma catástrofe em um mundo antes mesmo que o arquiteto da tragédia movesse suas peças. As pessoas em geral tem mais fé em suas habilidades precognitivas.",
                    "Proteção Inusitada - Combatendo uma invasão dos extragaláticos Tyranids em um planeta recém colonizado, você conseguiu combater a presença sufocante da mente de colméia das criaturas por preciosos segundos, permitindo que as comunicações saíssem para fora do sistema e reforços fossem contactados. Você possui fortíssimas barreiras mentais."
                ],
                "Vergonhas": [
                    "Toque do Abismo - Por algum motivo ou outro, as entidades do Mar de Almas parecem especificamente atraídas à sua pessoa. Em dúzias de viagens entre as estrelas, a nave que lhe transportava foi pega em tempestades tenebrosas ou mesmo abordadas por legiões de demônios e demais entidades desconhecidas. Capitães e marinheiros em geral sentem sua presença em naves como um mal agouro.",
                    "Tentação - Apesar de seu tremendo treinamento, seus encontros com as forças do Caos em si ainda revelam desejos seus, por poder, por grandeza. Você sempre conseguiu manter o controle e manter-se leal, mas sente cada vez mais sua mente fugindo. Você sente um enorme conflito dentro de si mesmo ao se deparar com entidades do Caos, que buscam te converter para os Poderes Ruinosos.",
                    "Perca de Controle - Em meio à uma batalha caótica, seus esforços para elevar seus poderes ao máximo passaram do limite, e um sargento dos Ultramarines que comandava boa parte das forças aliadas foi levado ao outro mundo em meio à raios e chamas negras invocadas por sua mente. Desde então, todos são apreensivos quanto ao seu uso de suas habilidades."
                ]
            },
            "img": "https://wh40k.lexicanum.com/mediawiki/images/thumb/f/fb/Miguel-iglesias-darktide-psyker-protectorate.jpg/665px-Miguel-iglesias-darktide-psyker-protectorate.jpg",
            "width": 330,
            "height": 450,
        },

        "Veterano da Guarda Imperial": {
            "Status": {
                "Vida": 3,
                "Iniciativa": 3,
                "Armadura": 1,
                "Perícia": 3,
                "Moral": 2
            },
            "Habilidades": {
                "Conhecimento (Império)": 1,
                "Conhecimento (Caos)": 1,
                "Conhecimento (Aliens)": 2,
                "Técnico": 2,
                "Carisma": 3,
                "Percepção": 1,
                "Resistência": 1,
                "Atleticismo": 2
            },
            "Nativas": [
                "Os Melhores do Imperador - O Veterano recebe um bônus de +2 em qualquer interação de história com personagens humanos 'normais' (não psíquico ou nulo, não modificado genéticamente ou mecanicamente)",
                "Kit Médico - Uma vez por batalha, o Veterano pode curar qualquer membro da party, restaurando 2 pontos de Vida",
                "Experiência de Mil Batalhas - Caso uma batalha comece com a decisão de Iniciativa favorecendo os inimigos, o membro da party com maior iniciativa passará a ter o primeiro turno, ignorando Iniciativa",
                "Subestimando a Guarda - Uma vez por batalha, quando um inimigo utilizar um ataque que tenha múltiplos alvos, se o Veterano for um desses alvos, ele não será atacado"
            ],
            "Combate": {
                "Ações": 3,
                "Habilidades": [
                    "Arma Melta (3 ações): Acerto 7+, Dano 2, Alvos 1 - Após o dano, o inimigo terá sua Armadura reduzida em -1 até o início do próximo turno do Veterano",
                    "Lança-Chamas (3 ações): Acerto 6+, Dano 2, Alvos 2 - Este ataque ignora o rolamento de Armadura",
                    "Fuzil Laser (2 ações): Acerto 5+, Dano 1, Alvos 1 - Cause 2 de Dano caso o inimigo tenha causado dano ao Veterano em seu último turno",
                    "Granada (2 ações): Acerto 6+, Dano 1, Alvos Todos",
                    "Disparo Singular (1 ação): Acerto 5+, Dano 1, Alvos 1",
                    "Faca de Combate (1 ação) [Ataque Corporal]: Acerto 4+, Dano 1, Alvos 1"
                ]
            },
            "Customização": {
                "Gênero": "Masculino/Feminino",
                "Opções de Nativa Bônus": [
                    "O Planeta Quebrou Antes que a Guarda Quebrasse - Caso seja o último membro da party vivo, o Veterano fica imune a testes de Moral, e recebe +1 em Perícia e Iniciativa",
                    "Disciplina Exemplar - O primeiro ataque do Veterano em cada turno recebe um bônus de +1 no dado de Acerto"
                ],
                "Triunfos": [
                    "Soldado Decisivo - Em uma campanha crucial, contra toda a sorte, apenas você segurou uma fortificação contra um batalhão inimigo por cruciais minutos, permitindo que reforços de fora do planeta fizessem a aterrisagem e erradicassem os inimigos. Membros do Império de patente superior à sua são mais favoráveis, e passíveis de compartilhar informação estratégica.",
                    "Defensor do Povo - Você liderou um contingente de sobreviventes para a segurança em meio ao campo de batalha, virando um ícone de esperança e respeito no planeta do conflito. Consegue reconhecer pedidos de ajuda mesmo em uma zona de guerra, e tentar resgatar aqueles afetados.",
                    "Indomável - Quando sua munição já estava esgotada, manteve sua compostura e atacou invasores aliens com sua simples faca. Sua natureza inabalável perante forças insuperáveis lhe ganhou o respeito de vários contingentes de Marines que vieram a testemunhar sua batalha."
                ],
                "Vergonhas": [
                    "Vitória Questionável - Numa batalha sem chances de vitória, o batalhão do qual você fazia parte ficou pasmo com uma repentina intervenção de aliens - os Eldar - que dizimaram a força traidora inimiga sem explicação aparente, desaparecendo tão rapidamente quanto apareceram. Apesar do resultado positivo, oficiais da Inquisição não deixaram de notar sua 'aliança' aos aliens, mesmo não sendo por sua escolha.",
                    "Capturado e Atormentado - Após uma derrota, você estava entre os capturados por Marines traidores. Os hereges fizeram todo tipo de tortura para tentar converter você e seus companheiros, e as cicatrizes ainda doem e tremem toda vez que você vê um Marine, mesmo o mais leal deles.",
                    "Covarde Aparente - Apesar de sua inegável eficácia em combate, sempre que os comissários e oficiais mencionavam um conflito contra os inimigos do Império seu primeiro instinto era tentar evitar o combate, prática que não obteve muito sucesso. Independentemente, você não lida bem com a ideia de uma batalha próxima."
                ]
            },
            "img": "https://wh40k.lexicanum.com/mediawiki/images/thumb/0/05/KasrkinArtPlasma.jpg/521px-KasrkinArtPlasma.jpg",
            "width": 260,
            "height": 450,
        }
    }
    return classes_data
