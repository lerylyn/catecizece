import streamlit as st
from typing import Dict, List, Any

# ============================================================
# CONFIGURAÇÃO DA PÁGINA E TEMA
# ============================================================
st.set_page_config(
    page_title="Catequese em Comunhão | Formação para Adolescentes",
    page_icon="✝️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado - visual claro, limpo e acolhedor
st.markdown("""
<style>
    /* Fundo geral claro */
    .stApp {
        background-color: #f8fafc;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #1e3a5f;
    }
    [data-testid="stSidebar"] * {
        color: #f1f5f9 !important;
    }
    [data-testid="stSidebar"] .stRadio label {
        color: #e2e8f0 !important;
    }
    
    /* Títulos */
    h1, h2, h3 {
        color: #1e3a5f !important;
        font-family: 'Segoe UI', system-ui, sans-serif;
    }
    
    /* Cards de conteúdo */
    .content-card {
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 2px 8px rgba(30, 58, 95, 0.08);
        border-left: 5px solid #3b82f6;
    }
    
    .quiz-card {
        background: #eff6ff;
        border-radius: 12px;
        padding: 1.25rem;
        margin-top: 1rem;
        border: 1px solid #bfdbfe;
    }
    
    .saint-card, .miracle-card, .apparition-card {
        background: white;
        border-radius: 10px;
        padding: 1.1rem;
        margin-bottom: 0.8rem;
        box-shadow: 0 1px 4px rgba(0,0,0,0.06);
        border-left: 4px solid #60a5fa;
    }
    
    .ref-box {
        background: #f1f5f9;
        border-radius: 8px;
        padding: 0.75rem 1rem;
        font-size: 0.9rem;
        color: #334155;
        margin: 0.8rem 0;
    }
    
    .success-msg {
        background: #dcfce7;
        color: #166534;
        padding: 0.75rem;
        border-radius: 8px;
        font-weight: 500;
    }
    
    .error-msg {
        background: #fee2e2;
        color: #991b1b;
        padding: 0.75rem;
        border-radius: 8px;
    }
    
    /* Botões */
    .stButton>button {
        border-radius: 8px;
        font-weight: 500;
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        font-weight: 600;
        color: #1e3a5f;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================
# DADOS DOS TEMAS (resumo adaptado para adolescentes)
# ============================================================

# Estrutura: fase -> lista de temas com conteúdo completo em alguns
TEMAS_COMPLETOS: Dict[str, List[Dict[str, Any]]] = {
    "Catequese Infantil / Pré-Eucaristia": [
        {
            "titulo": "1. Que grande alegria, Jesus nasceu!",
            "resumo": """Jesus nasceu em Belém, num estábulo simples, porque não havia lugar na hospedaria. 
Ele é o Filho de Deus que se fez criança como nós para estar perto de nós. 
O Natal não é só presente e luzes: é a festa do amor de Deus que veio morar conosco. 
Maria e José acolheram Jesus com muito amor. Nós também somos convidados a abrir o coração para Ele.""",
            "biblia": "Lc 2,1-20; Jo 1,14; Mt 1,18-25",
            "catecismo": "CIC 422-424, 525-526 (O mistério da Encarnação e o Natal)",
            "quiz": [
                {
                    "pergunta": "Por que Jesus nasceu num estábulo?",
                    "opcoes": ["Porque queria ser rico", "Porque não havia lugar na hospedaria e Deus escolheu a simplicidade", "Porque Maria e José preferiram", "Porque era tradição"],
                    "correta": 1
                },
                {
                    "pergunta": "O que significa 'Encarnação'?",
                    "opcoes": ["Jesus virou anjo", "O Filho de Deus se fez homem de verdade", "Só uma história bonita", "Um milagre de Natal"],
                    "correta": 1
                },
                {
                    "pergunta": "Qual é a melhor forma de celebrar o Natal segundo a fé?",
                    "opcoes": ["Só trocando presentes", "Abrindo o coração para Jesus e vivendo o amor", "Decorando a casa", "Comendo bastante"],
                    "correta": 1
                }
            ]
        },
        {
            "titulo": "2. Jesus é nosso amigo",
            "resumo": """Jesus não é só uma pessoa do passado. Ele é vivo e quer ser nosso amigo de verdade. 
Um amigo de verdade escuta, ajuda, perdoa e nunca abandona. Jesus faz tudo isso. 
Ele disse: “Já não vos chamo servos, mas amigos” (Jo 15,15). 
Podemos conversar com Ele a qualquer momento, na oração, e Ele sempre nos escuta.""",
            "biblia": "Jo 15,13-15; Mt 11,28-30; Jo 14,6",
            "catecismo": "CIC 422, 426, 1698 (Amizade com Cristo)",
            "quiz": [
                {
                    "pergunta": "O que Jesus disse sobre a amizade conosco?",
                    "opcoes": ["Só os santos podem ser amigos dEle", "Já não vos chamo servos, mas amigos", "Amizade é só entre pessoas", "Precisa de mérito especial"],
                    "correta": 1
                },
                {
                    "pergunta": "Como podemos cultivar a amizade com Jesus?",
                    "opcoes": ["Só na missa de domingo", "Conversando com Ele na oração e vivendo o amor", "Memorizando orações longas", "Evitar pecados apenas"],
                    "correta": 1
                },
                {
                    "pergunta": "Jesus promete o que para quem vai até Ele?",
                    "opcoes": ["Riqueza", "Descanso e alívio (Mt 11,28)", "Fama", "Poder"],
                    "correta": 1
                }
            ]
        },
        {
            "titulo": "5. É preciso amar de verdade",
            "resumo": """Amar de verdade não é só gostar ou sentir carinho. É querer o bem do outro, mesmo quando custa. 
Jesus ensinou o mandamento novo: “Amai-vos uns aos outros como eu vos amei” (Jo 13,34). 
O amor verdadeiro inclui respeito, perdão, generosidade e paciência. 
Não é sentimento passageiro: é decisão de cada dia.""",
            "biblia": "Jo 13,34-35; 1Cor 13,1-13; Mt 22,37-40",
            "catecismo": "CIC 1822-1829 (A caridade)",
            "quiz": [
                {
                    "pergunta": "Qual é o mandamento novo de Jesus?",
                    "opcoes": ["Rezar muito", "Amai-vos uns aos outros como eu vos amei", "Ir à missa todo dia", "Dar esmola"],
                    "correta": 1
                },
                {
                    "pergunta": "Segundo 1Cor 13, o que é o maior de todos?",
                    "opcoes": ["A fé", "A esperança", "O amor (caridade)", "O conhecimento"],
                    "correta": 2
                },
                {
                    "pergunta": "Amar de verdade significa principalmente:",
                    "opcoes": ["Sentir emoção forte", "Querer o bem do outro e agir por ele", "Gostar de todo mundo", "Evitar discussões"],
                    "correta": 1
                }
            ]
        },
        {
            "titulo": "10. Devemos perdoar sempre",
            "resumo": """Perdoar não é esquecer o que aconteceu nem dizer que não doeu. 
É decidir não guardar rancor e deixar Deus curar o coração. 
Jesus perdoou na cruz e nos ensinou a rezar: “Perdoai-nos as nossas ofensas, assim como nós perdoamos...”. 
Quando perdoamos, ficamos livres. Quando não perdoamos, o rancor nos prende.""",
            "biblia": "Mt 6,12-15; Mt 18,21-35; Lc 23,34",
            "catecismo": "CIC 2840-2845 (O perdão)",
            "quiz": [
                {
                    "pergunta": "Quantas vezes Jesus disse que devemos perdoar?",
                    "opcoes": ["Só uma vez", "Sete vezes", "Setenta vezes sete (sempre)", "Só se a pessoa pedir"],
                    "correta": 2
                },
                {
                    "pergunta": "Perdoar significa:",
                    "opcoes": ["Esquecer tudo e fingir que nada aconteceu", "Não guardar rancor e deixar Deus agir", "Deixar a pessoa fazer de novo", "Ser fraco"],
                    "correta": 1
                },
                {
                    "pergunta": "O que Jesus fez na cruz em relação aos que o matavam?",
                    "opcoes": ["Pediu vingança", "Perdoou-os", "Ficou em silêncio", "Chamou os anjos"],
                    "correta": 1
                }
            ]
        },
        {
            "titulo": "18. Ele está vivo no meio de nós!",
            "resumo": """Jesus ressuscitou no terceiro dia. A morte não teve a última palavra. 
Ele está vivo e presente: na Eucaristia, na Palavra, na comunidade e no coração de quem crê. 
A Páscoa é a festa mais importante da Igreja porque celebra a vida nova que Jesus nos deu. 
Nós também somos convidados a “ressuscitar” cada dia: deixar o egoísmo e viver o amor.""",
            "biblia": "Lc 24; Jo 20-21; 1Cor 15,3-8",
            "catecismo": "CIC 638-658 (A Ressurreição de Cristo)",
            "quiz": [
                {
                    "pergunta": "Qual é a festa mais importante da Igreja?",
                    "opcoes": ["Natal", "Páscoa (Ressurreição)", "Pentecostes", "Corpus Christi"],
                    "correta": 1
                },
                {
                    "pergunta": "Onde Jesus continua presente de modo especial?",
                    "opcoes": ["Só no céu", "Na Eucaristia, na Palavra e na comunidade", "Apenas nas aparições", "Só nos santos"],
                    "correta": 1
                },
                {
                    "pergunta": "A Ressurreição significa que:",
                    "opcoes": ["Jesus voltou como fantasma", "A morte foi vencida e a vida nova começou", "Foi só uma metáfora", "Os discípulos inventaram"],
                    "correta": 1
                }
            ]
        }
    ],
    "1ª Etapa da Eucaristia": [
        {
            "titulo": "Bloco 1 – Jesus quer ser meu amigo | 2. Amigos de Jesus",
            "resumo": """Ser amigo de Jesus é o começo de tudo na catequese. 
Ele nos escolheu primeiro. Não precisamos ser perfeitos para nos aproximarmos dEle. 
Na turma de catequese aprendemos juntos a caminhar com Jesus. 
A amizade com Ele muda o jeito de olhar as pessoas, a família e a vida.""",
            "biblia": "Jo 15,15; Mc 3,13-15; Jo 1,35-39",
            "catecismo": "CIC 426, 520, 1698",
            "quiz": [
                {
                    "pergunta": "Quem escolheu primeiro a amizade: nós ou Jesus?",
                    "opcoes": ["Nós", "Jesus (Ele nos escolheu)", "Depende", "Os pais"],
                    "correta": 1
                },
                {
                    "pergunta": "Para ser amigo de Jesus é preciso:",
                    "opcoes": ["Ser santo primeiro", "Abrir o coração e querer caminhar com Ele", "Saber todas as orações", "Ir à missa todo dia"],
                    "correta": 1
                },
                {
                    "pergunta": "A catequese ajuda principalmente a:",
                    "opcoes": ["Decorar regras", "Crescer na amizade com Jesus em comunidade", "Ganhar prêmios", "Fazer amigos só"],
                    "correta": 1
                }
            ]
        },
        {
            "titulo": "Bloco 1 – 3. Bíblia, um caminho para conhecer Jesus",
            "resumo": """A Bíblia não é um livro qualquer. É a Palavra de Deus que nos fala hoje. 
Nela conhecemos quem é Jesus, o que Ele fez e o que Ele quer de nós. 
A Edição Pastoral ajuda a entender melhor o contexto e o sentido das palavras. 
Quando lemos a Bíblia com fé e oração, Jesus se torna mais próximo.""",
            "biblia": "2Tm 3,16-17; Lc 24,27; Jo 5,39",
            "catecismo": "CIC 101-141 (A Sagrada Escritura)",
            "quiz": [
                {
                    "pergunta": "O que é a Bíblia para os cristãos?",
                    "opcoes": ["Um livro de histórias antigas", "A Palavra de Deus inspirada", "Só o Novo Testamento", "Um manual de regras"],
                    "correta": 1
                },
                {
                    "pergunta": "Qual parte da Bíblia fala mais diretamente de Jesus?",
                    "opcoes": ["Só o Antigo Testamento", "Os Evangelhos (Novo Testamento)", "Só as cartas de Paulo", "O Apocalipse"],
                    "correta": 1
                },
                {
                    "pergunta": "Como devemos ler a Bíblia?",
                    "opcoes": ["Só como literatura", "Com fé, oração e ajuda da Igreja", "Rapidamente", "Só os trechos bonitos"],
                    "correta": 1
                }
            ]
        },
        {
            "titulo": "Bloco 2 – 4. Maria, Mãe de Jesus",
            "resumo": """Maria é a mãe de Jesus e também nossa mãe espiritual. 
Ela disse “sim” a Deus com toda a liberdade e confiança. 
No Evangelho ela aparece sempre apontando para o Filho: “Fazei tudo o que Ele vos disser” (Jo 2,5). 
Rezar a Ave-Maria e o Terço nos ajuda a ficar perto de Jesus com o coração de Maria.""",
            "biblia": "Lc 1,26-38; Jo 2,1-11; Jo 19,25-27",
            "catecismo": "CIC 484-511, 963-975 (Maria)",
            "quiz": [
                {
                    "pergunta": "Qual foi a resposta de Maria ao anjo?",
                    "opcoes": ["Não estou preparada", "Faça-se em mim segundo a tua palavra (sim)", "Depois eu vejo", "Preciso pensar"],
                    "correta": 1
                },
                {
                    "pergunta": "O que Maria disse nas bodas de Caná?",
                    "opcoes": ["Resolvam vocês", "Fazei tudo o que Ele vos disser", "Não tem mais vinho, acabou", "Vamos embora"],
                    "correta": 1
                },
                {
                    "pergunta": "Maria é:",
                    "opcoes": ["Só mãe de Jesus", "Mãe de Jesus e mãe nossa na ordem da graça", "Uma santa qualquer", "Deusa"],
                    "correta": 1
                }
            ]
        },
        {
            "titulo": "Bloco 3 – 12. Jesus nos ensina a rezar",
            "resumo": """Jesus rezava sempre: de manhã, à noite, antes de decisões importantes. 
Ele nos ensinou o Pai-Nosso, a oração perfeita. 
Rezar não é só pedir coisas. É conversar com o Pai, agradecer, pedir perdão e ouvir. 
Quando não sabemos o que dizer, o Espírito Santo reza em nós.""",
            "biblia": "Mt 6,5-15; Lc 11,1-13; Rm 8,26",
            "catecismo": "CIC 2607-2615, 2759-2865 (A oração do Senhor)",
            "quiz": [
                {
                    "pergunta": "Qual oração Jesus ensinou aos discípulos?",
                    "opcoes": ["Ave-Maria", "Pai-Nosso", "Glória", "Credo"],
                    "correta": 1
                },
                {
                    "pergunta": "Rezar é principalmente:",
                    "opcoes": ["Pedir favores", "Conversar com Deus (louvor, pedido, escuta)", "Repetir palavras", "Ficar em silêncio absoluto"],
                    "correta": 1
                },
                {
                    "pergunta": "Quando não sabemos rezar, quem nos ajuda?",
                    "opcoes": ["Os anjos apenas", "O Espírito Santo", "Ninguém", "Os santos só"],
                    "correta": 1
                }
            ]
        },
        {
            "titulo": "Bloco 4 – 17. Jesus, doação e serviço",
            "resumo": """Jesus não veio para ser servido, mas para servir e dar a vida (Mc 10,45). 
Na Última Ceia Ele lavou os pés dos discípulos. 
Servir é o jeito de Jesus amar. Na catequese e na vida cristã aprendemos a servir a família, os amigos e os mais necessitados. 
O maior no Reino de Deus é aquele que serve.""",
            "biblia": "Mc 10,42-45; Jo 13,1-15; Mt 20,26-28",
            "catecismo": "CIC 608, 1570, 2235 (Serviço e autoridade)",
            "quiz": [
                {
                    "pergunta": "Jesus veio para:",
                    "opcoes": ["Ser rei poderoso na terra", "Servir e dar a vida em resgate", "Condenar os pecadores", "Fundar um império"],
                    "correta": 1
                },
                {
                    "pergunta": "O que Jesus fez na Última Ceia que surpreendeu os discípulos?",
                    "opcoes": ["Multiplicou pães", "Lavou os pés deles", "Subiu ao céu", "Chamou os fariseus"],
                    "correta": 1
                },
                {
                    "pergunta": "Quem é o maior no Reino de Deus?",
                    "opcoes": ["Quem manda mais", "Quem serve", "Quem sabe mais", "Quem é rico"],
                    "correta": 1
                }
            ]
        }
    ],
    "2ª Etapa da Eucaristia": [
        {
            "titulo": "Bloco 1 – 1. Jesus nos revela o Pai",
            "resumo": """Ninguém conhece o Pai a não ser o Filho e aquele a quem o Filho o quiser revelar (Mt 11,27). 
Jesus nos mostrou que Deus não é um juiz distante, mas um Pai bondoso que nos ama. 
Podemos chamá-Lo de “Abba” (papai). 
Conhecer o Pai muda a forma como nos vemos e como tratamos os outros.""",
            "biblia": "Mt 11,25-27; Jo 14,8-11; Lc 15,11-32",
            "catecismo": "CIC 238-242, 2777-2778",
            "quiz": [
                {
                    "pergunta": "Como Jesus nos ensinou a chamar a Deus?",
                    "opcoes": ["Senhor distante", "Pai (Abba)", "Juiz", "Criador apenas"],
                    "correta": 1
                },
                {
                    "pergunta": "Quem revela o Pai de modo completo?",
                    "opcoes": ["Os profetas", "Jesus, o Filho", "Os anjos", "A natureza"],
                    "correta": 1
                },
                {
                    "pergunta": "A parábola do Pai Misericordioso (filho pródigo) mostra que Deus:",
                    "opcoes": ["Castiga severamente", "Espera e acolhe com alegria quem volta", "Esquece os filhos", "Prefere os justos"],
                    "correta": 1
                }
            ]
        },
        {
            "titulo": "Bloco 2 – 7. Estabeleço minha aliança convosco!",
            "resumo": """Deus sempre quis uma aliança (pacto de amor) com o seu povo. 
No Antigo Testamento fez aliança com Noé, Abraão, Moisés. 
Jesus instituiu a Nova Aliança no seu sangue, na Eucaristia. 
Nós pertencemos a essa aliança pelo Batismo e a renovamos a cada Eucaristia.""",
            "biblia": "Gn 9,8-17; Ex 19-24; Lc 22,19-20; 1Cor 11,25",
            "catecismo": "CIC 54-64, 1961-1964, 1339",
            "quiz": [
                {
                    "pergunta": "O que é uma aliança na Bíblia?",
                    "opcoes": ["Um contrato comercial", "Um pacto de amor e fidelidade entre Deus e o povo", "Uma lei rigorosa", "Uma festa"],
                    "correta": 1
                },
                {
                    "pergunta": "Onde Jesus instituiu a Nova Aliança?",
                    "opcoes": ["No Batismo", "Na Última Ceia (Eucaristia)", "Na Cruz apenas", "No Pentecostes"],
                    "correta": 1
                },
                {
                    "pergunta": "Pelo Batismo nós:",
                    "opcoes": ["Só recebemos um nome", "Entramos na Nova Aliança", "Ficamos isentos de pecados futuros", "Viramos anjos"],
                    "correta": 1
                }
            ]
        },
        {
            "titulo": "Bloco 3 – 13. Os mandamentos guiam meu olhar para Deus",
            "resumo": """Os Dez Mandamentos não são regras para nos prender. São caminhos de liberdade e felicidade. 
Os três primeiros falam da relação com Deus: amá-Lo acima de tudo, respeitar o nome dEle e guardar o dia do Senhor. 
Quando colocamos Deus em primeiro lugar, o resto da vida se organiza melhor.""",
            "biblia": "Ex 20,1-11; Dt 5,6-15; Mt 22,37",
            "catecismo": "CIC 2083-2195 (1º ao 3º mandamento)",
            "quiz": [
                {
                    "pergunta": "Os três primeiros mandamentos tratam principalmente de:",
                    "opcoes": ["Relação com o próximo", "Relação com Deus", "Regras de higiene", "Política"],
                    "correta": 1
                },
                {
                    "pergunta": "O que significa “não ter outros deuses”?",
                    "opcoes": ["Não gostar de esportes", "Não colocar nada acima de Deus (dinheiro, fama, prazer...)", "Não ter amigos", "Não usar celular"],
                    "correta": 1
                },
                {
                    "pergunta": "Guardar o dia do Senhor significa principalmente:",
                    "opcoes": ["Dormir o dia todo", "Participar da Eucaristia e descansar em Deus", "Trabalhar mais", "Fazer compras"],
                    "correta": 1
                }
            ]
        },
        {
            "titulo": "Bloco 4 – 20. Maria, a Nova Arca da Aliança",
            "resumo": """No Antigo Testamento a Arca da Aliança guardava a presença de Deus. 
Maria carregou em seu ventre o próprio Filho de Deus. Por isso a Igreja a chama de Nova Arca da Aliança. 
Ela é modelo de quem acolhe a Palavra e a faz vida. 
Em Aparecida e em tantas devoções, o povo brasileiro reconhece Maria como mãe que nos leva a Jesus.""",
            "biblia": "Lc 1,39-56; Ap 11,19–12,1; 2Sm 6",
            "catecismo": "CIC 2676, 2677, 2853",
            "quiz": [
                {
                    "pergunta": "Por que Maria é chamada Nova Arca da Aliança?",
                    "opcoes": ["Porque era de ouro", "Porque carregou em si o Filho de Deus", "Porque morava no templo", "Porque era rainha"],
                    "correta": 1
                },
                {
                    "pergunta": "O Magnificat (Lc 1) é:",
                    "opcoes": ["Uma oração de pedido", "O cântico de louvor de Maria", "Uma profecia de castigo", "Um salmo de Davi"],
                    "correta": 1
                },
                {
                    "pergunta": "Maria sempre nos aponta para:",
                    "opcoes": ["Ela mesma", "Jesus", "Os anjos", "Os santos"],
                    "correta": 1
                }
            ]
        }
    ],
    "3ª Etapa da Eucaristia": [
        {
            "titulo": "Bloco 1 – 4. Somos Igreja, povo de Deus",
            "resumo": """A Igreja não é só o prédio nem só os padres. Somos nós, o povo de Deus batizado. 
Jesus quis uma comunidade: “Onde dois ou três estiverem reunidos em meu nome, eu estou no meio deles”. 
Cada um tem um lugar e um carisma. Ninguém sobra. 
Ser Igreja é caminhar juntos, rezar juntos e servir juntos.""",
            "biblia": "1Pd 2,9-10; Mt 18,20; Ef 4,1-16",
            "catecismo": "CIC 781-786, 897-913 (Povo de Deus e leigos)",
            "quiz": [
                {
                    "pergunta": "A Igreja é principalmente:",
                    "opcoes": ["Um prédio bonito", "O povo de Deus reunido em Cristo", "Só os padres e bispos", "Uma ONG"],
                    "correta": 1
                },
                {
                    "pergunta": "Quem faz parte da Igreja?",
                    "opcoes": ["Só os religiosos", "Todos os batizados", "Só quem vai à missa todo dia", "Só os santos"],
                    "correta": 1
                },
                {
                    "pergunta": "O que significa “povo de Deus”?",
                    "opcoes": ["Um povo escolhido para se achar melhor", "Aqueles que Deus chamou para serem seus e servirem o mundo", "Uma nação política", "Os judeus apenas"],
                    "correta": 1
                }
            ]
        },
        {
            "titulo": "Bloco 2 – 12. Comam, bebam, isto é o meu Corpo, isto é o meu Sangue",
            "resumo": """Na Última Ceia Jesus instituiu a Eucaristia. 
O pão e o vinho se tornam verdadeiramente o Corpo e o Sangue de Cristo. 
Não é só símbolo: é presença real. 
Receber a Comunhão é receber Jesus. Por isso nos preparamos com fé, respeito e, quando necessário, com a Confissão.""",
            "biblia": "Mt 26,26-29; Mc 14,22-25; Lc 22,19-20; Jo 6,51-58; 1Cor 11,23-26",
            "catecismo": "CIC 1322-1419 (A Eucaristia)",
            "quiz": [
                {
                    "pergunta": "O que acontece na consagração?",
                    "opcoes": ["O pão e o vinho ficam só simbolizando", "Tornam-se verdadeiramente Corpo e Sangue de Cristo", "Ficam abençoados apenas", "Nada especial"],
                    "correta": 1
                },
                {
                    "pergunta": "Por que nos preparamos antes de comungar?",
                    "opcoes": ["Por tradição", "Porque recebemos o próprio Jesus e devemos estar em estado de graça", "Para parecer bem", "Porque o padre exige"],
                    "correta": 1
                },
                {
                    "pergunta": "A Eucaristia é:",
                    "opcoes": ["Só uma refeição comunitária", "Memorial da Paixão, presença real e banquete do Reino", "Apenas um rito antigo", "Uma lembrança simbólica"],
                    "correta": 1
                }
            ]
        },
        {
            "titulo": "Bloco 3 – 15. No Reino de Deus existe perdão",
            "resumo": """Deus não se cansa de perdoar. Nós é que nos cansamos de pedir perdão. 
O sacramento da Reconciliação (Confissão) é o encontro com a misericórdia de Deus. 
Não é humilhação: é libertação. 
Jesus deu aos apóstolos o poder de perdoar pecados. Hoje os padres exercem esse ministério em nome de Cristo.""",
            "biblia": "Jo 20,21-23; Lc 15; Mt 18,21-22",
            "catecismo": "CIC 1422-1498 (Sacramento da Penitência)",
            "quiz": [
                {
                    "pergunta": "O sacramento da Reconciliação serve para:",
                    "opcoes": ["Humilhar a pessoa", "Reencontrar a amizade com Deus e a liberdade interior", "Contar fofocas", "Pagar penitência pesada"],
                    "correta": 1
                },
                {
                    "pergunta": "Quem tem o poder de perdoar pecados na Igreja?",
                    "opcoes": ["Qualquer cristão", "Os padres e bispos em nome de Cristo", "Só o Papa", "Ninguém mais"],
                    "correta": 1
                },
                {
                    "pergunta": "Deus se cansa de perdoar?",
                    "opcoes": ["Sim, depois de muitas vezes", "Não, a misericórdia dEle é infinita", "Só perdoa pecados leves", "Depende do humor"],
                    "correta": 1
                }
            ]
        },
        {
            "titulo": "Bloco 4 – 20. Estando a caminho, explicou-lhes as Escrituras e colocou-se à mesa com eles",
            "resumo": """No caminho de Emaús os discípulos estavam tristes. Jesus se aproximou, explicou as Escrituras e partiu o pão. 
Aí os olhos deles se abriram. 
A missa é exatamente isso: Palavra + Eucaristia. 
Quando ouvimos a Palavra e comungamos, Jesus caminha conosco e nosso coração arde.""",
            "biblia": "Lc 24,13-35",
            "catecismo": "CIC 1329, 1346-1347, 1391",
            "quiz": [
                {
                    "pergunta": "O que aconteceu no caminho de Emaús?",
                    "opcoes": ["Os discípulos reconheceram Jesus na fração do pão", "Jesus sumiu para sempre", "Eles ficaram com raiva", "Não aconteceu nada"],
                    "correta": 0
                },
                {
                    "pergunta": "A estrutura da Missa lembra Emaús porque tem:",
                    "opcoes": ["Só canto", "Liturgia da Palavra e Liturgia Eucarística", "Só pregação", "Só comunhão"],
                    "correta": 1
                },
                {
                    "pergunta": "O que os discípulos sentiram enquanto Jesus falava?",
                    "opcoes": ["Sono", "O coração ardia", "Medo", "Indiferença"],
                    "correta": 1
                }
            ]
        }
    ],
    "Catequese Crismal / Perseverança": [
        {
            "titulo": "1. O homem: centro de atenção de Deus",
            "resumo": """Deus criou o ser humano à sua imagem e semelhança. 
Somos o ponto alto da criação. Temos dignidade que ninguém pode tirar. 
Isso vale para todo mundo: rico ou pobre, saudável ou doente, amigo ou desconhecido. 
Respeitar a dignidade humana é consequência direta da fé.""",
            "biblia": "Gn 1,26-31; Salmo 8; Mt 25,31-46",
            "catecismo": "CIC 355-384, 1700-1709",
            "quiz": [
                {
                    "pergunta": "O ser humano foi criado:",
                    "opcoes": ["Por acaso", "À imagem e semelhança de Deus", "Só para trabalhar", "Inferior aos anjos em tudo"],
                    "correta": 1
                },
                {
                    "pergunta": "A dignidade da pessoa humana:",
                    "opcoes": ["Depende do que ela produz", "É inerente e inviolável", "Só existe para os batizados", "Pode ser tirada pelo Estado"],
                    "correta": 1
                },
                {
                    "pergunta": "Como devemos tratar os outros segundo essa verdade?",
                    "opcoes": ["Com indiferença", "Com respeito e cuidado, especialmente os mais frágeis", "Só os que pensam como nós", "Com superioridade"],
                    "correta": 1
                }
            ]
        },
        {
            "titulo": "15. A fé em Jesus",
            "resumo": """A fé não é só acreditar que Deus existe. É confiar em Jesus, aderir a Ele com a vida. 
A fé é dom de Deus e também resposta nossa. 
Ela cresce na oração, na escuta da Palavra, nos sacramentos e na vida comunitária. 
A Crisma fortalece essa fé para sermos testemunhas.""",
            "biblia": "Hb 11,1; Rm 10,17; Mc 9,23-24; Jo 20,29",
            "catecismo": "CIC 142-184, 2087-2089",
            "quiz": [
                {
                    "pergunta": "A fé cristã é principalmente:",
                    "opcoes": ["Acreditar que Deus existe", "Adesão pessoal a Jesus Cristo e ao seu Evangelho", "Saber o Catecismo de cor", "Ir à missa"],
                    "correta": 1
                },
                {
                    "pergunta": "De onde vem a fé?",
                    "opcoes": ["Só do nosso esforço", "É dom de Deus e resposta humana", "Da inteligência apenas", "Da família só"],
                    "correta": 1
                },
                {
                    "pergunta": "A Crisma tem relação com a fé porque:",
                    "opcoes": ["Substitui o Batismo", "Fortalece a fé para a missão e o testemunho", "É só uma festa", "É opcional"],
                    "correta": 1
                }
            ]
        },
        {
            "titulo": "19. Jesus Cristo e o Espírito Santo",
            "resumo": """O Espírito Santo é a terceira Pessoa da Trindade. 
Ele foi prometido por Jesus e veio no Pentecostes. 
Na Crisma somos ungidos com o Crisma e recebemos uma efusão especial do Espírito. 
Os dons do Espírito (sabedoria, entendimento, conselho, fortaleza, ciência, piedade e temor de Deus) nos ajudam a viver como discípulos.""",
            "biblia": "Jo 14,15-26; At 2,1-13; Is 11,1-3; 1Cor 12",
            "catecismo": "CIC 683-747, 1285-1321 (Confirmação)",
            "quiz": [
                {
                    "pergunta": "Quem é o Espírito Santo?",
                    "opcoes": ["Uma força impessoal", "A terceira Pessoa da Santíssima Trindade", "Um anjo superior", "O mesmo que Jesus"],
                    "correta": 1
                },
                {
                    "pergunta": "O que acontece na Crisma?",
                    "opcoes": ["Só uma bênção", "Ungimos com o Crisma e recebemos o Espírito de modo especial", "Mudamos de nome", "Terminamos a catequese"],
                    "correta": 1
                },
                {
                    "pergunta": "Quantos são os dons do Espírito Santo tradicionalmente enumerados?",
                    "opcoes": ["3", "7", "12", "9"],
                    "correta": 1
                }
            ]
        },
        {
            "titulo": "24. Sacramento da Confirmação",
            "resumo": """A Confirmação (Crisma) completa a graça do Batismo. 
Somos mais perfeitamente unidos à Igreja e enriquecidos com uma força especial do Espírito Santo. 
O sinal visível é a unção com o Santo Crisma na fronte, feita pelo bispo (ou padre autorizado). 
Não é o “fim” da catequese: é o início de uma vida mais consciente de discípulo missionário.""",
            "biblia": "At 8,14-17; At 19,5-6; 2Cor 1,21-22",
            "catecismo": "CIC 1285-1321",
            "quiz": [
                {
                    "pergunta": "A Crisma:",
                    "opcoes": ["Substitui o Batismo", "Confirma e fortalece a graça batismal", "É só para jovens", "É opcional para ser cristão completo"],
                    "correta": 1
                },
                {
                    "pergunta": "O sinal principal da Crisma é:",
                    "opcoes": ["A água", "A unção com o Santo Crisma", "O pão", "A imposição de mãos apenas"],
                    "correta": 1
                },
                {
                    "pergunta": "Depois da Crisma o cristão é chamado a:",
                    "opcoes": ["Parar de estudar a fé", "Ser testemunha e discípulo missionário", "Só rezar em casa", "Julgar os outros"],
                    "correta": 1
                }
            ]
        }
    ],
    "Catequese com Adultos (Querigma e Itinerário)": [
        {
            "titulo": "Querigma – 3. Jesus é o caminho para Deus",
            "resumo": """Jesus não é um caminho entre outros. Ele é “o Caminho, a Verdade e a Vida” (Jo 14,6). 
Ninguém vai ao Pai senão por Ele. 
O anúncio primeiro (querigma) é simples: Deus te ama, enviou o Filho que morreu e ressuscitou por ti, e te chama à conversão e à fé. 
Tudo o mais na catequese nasce desse anúncio.""",
            "biblia": "Jo 14,6; At 4,12; 1Cor 15,1-5",
            "catecismo": "CIC 422-429, 1698",
            "quiz": [
                {
                    "pergunta": "Jesus disse: “Eu sou o Caminho, a Verdade e a Vida”. Isso significa:",
                    "opcoes": ["Um caminho possível entre vários", "O único caminho definitivo para o Pai", "Uma metáfora bonita", "Só para os judeus"],
                    "correta": 1
                },
                {
                    "pergunta": "O que é o querigma?",
                    "opcoes": ["Um livro", "O primeiro anúncio da Boa-Nova de Jesus", "Uma oração", "Um sacramento"],
                    "correta": 1
                },
                {
                    "pergunta": "O núcleo do anúncio cristão é:",
                    "opcoes": ["Regras morais", "Jesus Cristo morto e ressuscitado por nós", "A história de Israel", "Os milagres"],
                    "correta": 1
                }
            ]
        },
        {
            "titulo": "Itinerário – 24. Os Sacramentos da Iniciação à Vida Cristã",
            "resumo": """Batismo, Confirmação e Eucaristia formam a iniciação cristã. 
Pelo Batismo nascemos para a vida nova. 
Pela Confirmação somos fortalecidos pelo Espírito. 
Pela Eucaristia somos alimentados e unidos a Cristo e à Igreja. 
Juntos eles nos inserem plenamente no mistério de Cristo.""",
            "biblia": "Mt 28,19-20; At 2,38; Jo 6,53-56",
            "catecismo": "CIC 1212, 1229-1233, 1285, 1322",
            "quiz": [
                {
                    "pergunta": "Quais são os sacramentos da Iniciação Cristã?",
                    "opcoes": ["Batismo, Confissão, Matrimônio", "Batismo, Confirmação e Eucaristia", "Ordem, Matrimônio, Unção", "Só o Batismo"],
                    "correta": 1
                },
                {
                    "pergunta": "O Batismo realiza principalmente:",
                    "opcoes": ["Uma festa de família", "O nascimento para a vida nova em Cristo", "A entrada na escola", "O perdão só dos pecados futuros"],
                    "correta": 1
                },
                {
                    "pergunta": "A Eucaristia na iniciação:",
                    "opcoes": ["É opcional", "Alimenta e aperfeiçoa a comunhão com Cristo", "Só para adultos", "Substitui os outros sacramentos"],
                    "correta": 1
                }
            ]
        }
    ]
}

# Lista completa de temas (para navegação)
LISTA_FASES = {
    "Catequese Infantil / Pré-Eucaristia": [
        "1. Que grande alegria, Jesus nasceu!", "2. Jesus é nosso amigo", "3. A Bíblia nos fala de Jesus",
        "4. Jesus nos chama a segui-Lo", "5. É preciso amar de verdade", "6. A partilha nos faz felizes",
        "7. Jesus, aumenta a nossa fé", "7b. Participar da Missa com minha família", "8. Com Jesus aprendemos a rezar",
        "8b. As orações que aprendemos com a Igreja", "9. Usar nossos talentos para o bem", "10. Devemos perdoar sempre",
        "11. Jesus curou o surdo", "12. Em ti, Jesus, posso confiar!", "13. Jesus e Maria na festa de casamento",
        "14. O cuidado de Jesus por nós", "15. Ser paciente com as pessoas", "16. Jesus não condena as riquezas",
        "17. A lição do pai bondoso", "18. Ele está vivo no meio de nós!", "19. Jesus nos mandou o Espírito Santo",
        "20. Convidados a viver em Comunidade"
    ],
    "1ª Etapa da Eucaristia": [
        "1. Minha turma de Catequese", "2. Amigos de Jesus", "3. Bíblia, um caminho para conhecer Jesus",
        "4. Maria, Mãe de Jesus", "5. O Pai nos envia seu Filho", "6. Crescer diante de Deus e dos homens",
        "7. Este é o meu Filho amado", "8. Jesus anuncia o Reino de Deus", "9. Palavras que falam ao coração",
        "10. Sinais de vida nova", "11. O jeito de Jesus acolher", "12. Jesus nos ensina a rezar",
        "13. Jesus nos ensina a perdoar", "14. Permanecei no meu amor", "15. Jesus nos ensina a ter compaixão",
        "16. Sou chamado a formar comunidade no amor", "17. Jesus, doação e serviço", "18. A cruz é sinal de amor",
        "19. Jesus está sempre conosco", "20. A Comunidade vive e celebra unida"
    ],
    "2ª Etapa da Eucaristia": [
        "1. Jesus nos revela o Pai", "2. Deus nos fala de muitas maneiras", "3. Deus fez todas as coisas",
        "4. Deus criou e entregou ao nosso cuidado", "5. Somos irmãos no amor de Deus", "6. Deus tem um plano para nos fazer felizes",
        "7. Estabeleço minha aliança convosco!", "8. Abraão, deixa a tua terra!", "9. Abraão, pai dos que creem",
        "10. Moisés, liberta o meu povo", "11. Deus nos prepara para sermos o seu povo", "12. Façam também vocês assim como eu",
        "13. Os mandamentos guiam meu olhar para Deus", "14. Os mandamentos guiam meu olhar para os irmãos",
        "15. Comunidade que nasce da Lei de Deus", "16. Davi, o pastor de ovelhas escolhido para ser rei",
        "17. Profetas, mensageiros do Deus verdadeiro", "18. Isaías, profeta da esperança", "19. Amós, profeta da justiça",
        "20. Maria, a Nova Arca da Aliança"
    ],
    "3ª Etapa da Eucaristia": [
        "1. Eis a nossa missão: anunciar a Boa-Nova a toda criatura", "2. O Espírito Santo anima a comunidade",
        "3. A Igreja nasce no coração de Jesus Cristo", "4. Somos Igreja, povo de Deus", "5. Somos o corpo de Cristo",
        "6. Rezemos ao Senhor", "7. Maria, mãe da Igreja", "8. Os Sacramentos são sinais de Deus em nossa vida",
        "9. Batismo, nascimento para comunidade", "10. Batizados: sal da terra e luz do mundo!",
        "11. Somos testemunhas de Cristo no mundo", "12. Comam, bebam, isto é o meu Corpo, isto é o meu Sangue",
        "13. O Pão da vida, a Comunhão", "14. Pecar é afastar-se de Deus", "15. No Reino de Deus existe perdão",
        "16. Reconciliados com Deus", "17. Bendito seja Deus que nos reuniu no amor de Cristo!",
        "18. Com Jesus caminhamos na Igreja", "19. Símbolos e gestos para a comunhão com Deus",
        "20. Estando a caminho, explicou-lhes as Escrituras e colocou-se à mesa com eles"
    ],
    "Catequese Crismal / Perseverança": [
        "1. O homem: centro de atenção de Deus", "2. Desvio de Rota", "3. Colaboradores de Deus",
        "4. Nosso sim a um viver diferente", "5. Ela viveu diferente – as atitudes de Maria",
        "6. Eles viveram de um jeito diferente", "7. Mandamentos, caminho do bem", "8. Deus em primeiro lugar",
        "9. Cada família é única!", "10. Em defesa da vida", "11. Amor e responsabilidade",
        "12. Ser honesto vale a pena?", "13. A cobiça nos tira a paz", "14. Caminho para a felicidade",
        "15. A fé em Jesus", "16. A vida ligada a Cristo Jesus", "17. A oração me faz íntimo do Senhor",
        "18. Na liturgia celebramos Jesus Cristo", "19. Jesus Cristo e o Espírito Santo",
        "20. Os sinais do amor de Deus", "21. Sacramentos da Iniciação Cristã", "22. Sacramentos de Cura",
        "23. Sacramentos de Serviço", "24. Sacramento da Confirmação"
    ],
    "Catequese com Adultos (Querigma e Itinerário)": [
        "Querigma: Vamos caminhar juntos", "Querigma: O que estamos procurando?", "Querigma: Jesus é o caminho para Deus",
        "Querigma: Jesus anuncia o reinado de Deus", "Querigma: Jesus se compadece e nos liberta",
        "Querigma: Jesus nos convida à conversão", "Itinerário: A Bíblia – Palavra viva de Deus",
        "Itinerário: A pessoa humana criada para ser feliz", "Itinerário: Jesus nasce em Belém",
        "Itinerário: Jesus inaugura o Reino de Deus", "Itinerário: A última ceia", "Itinerário: Deus Pai ressuscita Jesus",
        "Itinerário: O envio do Espírito Santo", "Itinerário: Os Sacramentos da Iniciação",
        "Itinerário: Os Sacramentos de cura e de serviço", "Itinerário: Somos discípulos missionários"
    ]
}

# ============================================================
# SANTOS
# ============================================================
SANTOS = [
    {"nome": "Nossa Senhora Aparecida", "onde": "Brasil", "resumo": "Padroeira do Brasil. A imagem foi encontrada em 1717 no rio Paraíba do Sul. Símbolo de fé, esperança e unidade do povo brasileiro."},
    {"nome": "São José de Anchieta", "onde": "Brasil (nascido na Espanha)", "resumo": "Apóstolo do Brasil, jesuíta, fundador de São Paulo e Rio de Janeiro. Evangelizou os indígenas com amor e aprendeu a língua tupi."},
    {"nome": "Santo Antônio de Sant’Anna Galvão (Frei Galvão)", "onde": "Brasil", "resumo": "Primeiro santo nascido no Brasil. Franciscano, fundou o Mosteiro da Luz. Conhecido pelas “pílulas de Frei Galvão” e pela intercessão em partos difíceis."},
    {"nome": "Santa Dulce dos Pobres (Irmã Dulce)", "onde": "Brasil", "resumo": "A “mãe dos pobres” de Salvador. Fundou hospitais e obras sociais. Canonizada em 2019. Exemplo de caridade heroica."},
    {"nome": "Santos Mártires de Cunhaú e Uruaçu", "onde": "Brasil", "resumo": "30 mártires (padres e leigos, incluindo crianças) mortos em 1645 no Rio Grande do Norte por causa da fé católica durante as invasões holandesas. Canonizados em 2017."},
    {"nome": "São Francisco de Assis", "onde": "Itália", "resumo": "Pobre de Assis. Amou a criação, os pobres e a Cruz. Fundador dos franciscanos. Padroeiro da ecologia."},
    {"nome": "Santa Teresinha do Menino Jesus", "onde": "França", "resumo": "Doutora da Igreja. Ensinou a “pequena via” da confiança e do amor nas coisas ordinárias. Padroeira das missões."},
    {"nome": "Santo Antônio de Pádua", "onde": "Portugal/Itália", "resumo": "Doutor da Igreja. Grande pregador. Conhecido no Brasil como santo casamenteiro e protetor dos pobres."},
    {"nome": "São Judas Tadeu", "onde": "Palestina", "resumo": "Apóstolo. Invocado nas causas impossíveis e desesperadas."},
    {"nome": "Santa Rita de Cássia", "onde": "Itália", "resumo": "Santa das causas impossíveis. Esposa, mãe, viúva e religiosa. Exemplo de paciência e perdão."},
    {"nome": "São Jorge", "onde": "Capadócia", "resumo": "Mártir. Guerreiro da fé. Muito popular no Brasil, especialmente no Rio de Janeiro."},
    {"nome": "São Sebastião", "onde": "Roma", "resumo": "Mártir flechado. Protetor contra epidemias e pestes. Padroeiro de muitas cidades brasileiras."},
    {"nome": "São José", "onde": "Palestina", "resumo": "Esposo de Maria e pai adotivo de Jesus. Padroeiro da Igreja Universal, dos trabalhadores e das famílias."},
    {"nome": "Santa Maria (Nossa Senhora)", "onde": "Palestina", "resumo": "Mãe de Deus e nossa Mãe. Modelo de fé, obediência e amor."},
    {"nome": "São Pedro", "onde": "Palestina", "resumo": "Apóstolo, primeiro Papa. A rocha sobre a qual Cristo edificou a Igreja."},
    {"nome": "São Paulo", "onde": "Tarso", "resumo": "Apóstolo dos gentios. Convertido no caminho de Damasco. Grande missionário e escritor."},
    {"nome": "Santo Agostinho", "onde": "Norte da África", "resumo": "Doutor da Igreja. De uma vida agitada à conversão radical. “Nosso coração está inquieto enquanto não repousa em Ti”."},
    {"nome": "São Tomás de Aquino", "onde": "Itália", "resumo": "Doutor Angélico. União profunda entre fé e razão. Autor da Suma Teológica."},
    {"nome": "Santa Catarina de Sena", "onde": "Itália", "resumo": "Doutora da Igreja. Mística e conselheira de papas. Amou a Igreja com paixão."},
    {"nome": "São João Paulo II", "onde": "Polônia", "resumo": "Papa da família, da juventude e da misericórdia. Viajou o mundo inteiro anunciando Cristo."},
    {"nome": "Santa Madre Teresa de Calcutá", "onde": "Albânia/Índia", "resumo": "Serviu os mais pobres dos pobres. “A paz começa com um sorriso”. Canonizada em 2016 (milagre brasileiro)."},
    {"nome": "São Maximiliano Kolbe", "onde": "Polônia", "resumo": "Deu a vida no lugar de um pai de família no campo de concentração de Auschwitz."},
    {"nome": "Santa Faustina Kowalska", "onde": "Polônia", "resumo": "Apóstola da Divina Misericórdia. Jesus revelou a ela a imagem e a festa da Misericórdia."},
    {"nome": "São Padre Pio", "onde": "Itália", "resumo": "Estigmatizado. Grande confessor e intercessor. “Rezai, esperai e não vos preocupeis”."},
    {"nome": "São João Bosco", "onde": "Itália", "resumo": "Pai e mestre da juventude. Fundador dos salesianos. Educou com amor e razão."},
    {"nome": "Santa Clara de Assis", "onde": "Itália", "resumo": "Amiga de São Francisco. Fundadora das Clarissas. Amou a pobreza e a Eucaristia."},
    {"nome": "São Bento", "onde": "Itália", "resumo": "Patriarca do monaquismo ocidental. “Ora et labora”. Padroeiro da Europa."},
    {"nome": "Santa Hildegarda de Bingen", "onde": "Alemanha", "resumo": "Doutora da Igreja. Mística, compositora, médica e escritora. Visão integral da criação."},
    {"nome": "São Carlos Acutis", "onde": "Itália (milagre no Brasil)", "resumo": "Primeiro santo millennial. Amou a Eucaristia e usou a internet para evangelizar. Milagre de cura reconhecido em Campo Grande-MS."},
    {"nome": "São Roque González e companheiros", "onde": "Missões (Brasil/Paraguai)", "resumo": "Jesuítas mártires das Reduções. Evangelizaram os indígenas com respeito e deram a vida."},
    {"nome": "Santa Teresa de Ávila", "onde": "Espanha", "resumo": "Doutora da Igreja. Grande mística e reformadora do Carmelo. “Deus sozinho basta”."},
    {"nome": "São João da Cruz", "onde": "Espanha", "resumo": "Doutor da Igreja. Mestre da noite escura e da união com Deus."},
    {"nome": "São Luís Maria Grignion de Montfort", "onde": "França", "resumo": "Apóstolo da consagração a Jesus por Maria. Grande influência na espiritualidade mariana."},
    {"nome": "Santa Edith Stein (Teresa Benedita da Cruz)", "onde": "Alemanha", "resumo": "Filósofa judia convertida, carmelita, mártir em Auschwitz. Doutora da Igreja."},
    {"nome": "São José Moscati", "onde": "Itália", "resumo": "Médico dos pobres. Uniu ciência e fé. Modelo para profissionais da saúde."},
]

# ============================================================
# MILAGRES
# ============================================================
MILAGRES = [
    {"titulo": "Milagre Eucarístico de Lanciano (Itália, séc. VIII)", "resumo": "Um sacerdote que duvidava da presença real viu a hóstia transformar-se em carne e o vinho em sangue. Estudos científicos modernos confirmaram que se trata de tecido cardíaco humano e sangue do tipo AB."},
    {"titulo": "Milagre de Bolsena-Orvieto (Itália, 1263)", "resumo": "Durante a Missa, a hóstia sangrou sobre o corporal. Este milagre inspirou o Papa Urbano IV a instituir a festa de Corpus Christi."},
    {"titulo": "Curas de Lourdes (França, desde 1858)", "resumo": "Centenas de curas inexplicáveis pela ciência foram reconhecidas pelo Bureau Médico de Lourdes. A água da gruta e a fé dos peregrinos são sinais da misericórdia de Deus através de Maria."},
    {"titulo": "Milagre do Sol em Fátima (Portugal, 13/10/1917)", "resumo": "Cerca de 70 mil pessoas viram o sol “dançar” e descer. Mesmo os céticos presentes relataram o fenômeno. Confirmou as aparições aos três pastorinhos."},
    {"titulo": "Sangue de São Januário (Nápoles)", "resumo": "Três vezes por ano o sangue coagulado do mártir se liquefaz diante do povo. Fenômeno observado há séculos e ainda sem explicação científica completa."},
    {"titulo": "Milagre da pesca e da imagem de Aparecida (Brasil, 1717)", "resumo": "Três pescadores encontraram o corpo e depois a cabeça de uma imagem de Nossa Senhora. Em seguida a pesca foi abundante. Início da maior devoção mariana do Brasil."},
    {"titulo": "Libertação do escravo Zacarias (Aparecida)", "resumo": "Um escravo fugitivo, acorrentado, passou perto da capela de Aparecida e as correntes se soltaram milagrosamente. Fortaleceu a fama de intercessora dos oprimidos."},
    {"titulo": "Cura de Matheus Vianna (Carlo Acutis – Brasil, 2013)", "resumo": "Menino de Campo Grande-MS com anomalia pancreática grave foi curado após contato com relíquia de Carlo Acutis. Milagre reconhecido para a beatificação do jovem santo."},
    {"titulo": "Cura do brasileiro Marcilio Haddad Andrino (Madre Teresa)", "resumo": "Brasileiro com múltiplos abscessos cerebrais em estado gravíssimo foi curado após orações a Madre Teresa. Milagre usado para sua canonização em 2016."},
    {"titulo": "Pílulas de Frei Galvão", "resumo": "O santo brasileiro escrevia uma oração em papéis que eram engolidos por gestantes e doentes. Inúmeros relatos de graças e partos seguros ao longo dos séculos. A tradição continua no Mosteiro da Luz."},
    {"titulo": "Incorruptibilidade de santos", "resumo": "Corpos de vários santos (Santa Bernadette, São Padre Pio, Santa Catarina de Bolonha etc.) permaneceram intactos ou pouco decompostos após a morte, sinal da graça divina."},
    {"titulo": "Milagres Eucarísticos contemporâneos", "resumo": "Casos em Buenos Aires (1996), Tixtla (México), Legnica (Polônia) e outros foram estudados e apresentaram tecido cardíaco humano com sinais de sofrimento, reforçando a fé na presença real."},
]

# ============================================================
# APARIÇÕES MARIANAS
# ============================================================
APARICOES = [
    {"titulo": "Nossa Senhora de Guadalupe (México, 1531)", "status": "Reconhecida", "resumo": "Apareceu a São Juan Diego. Deixou sua imagem milagrosa na tilma (manto). Padroeira da América e das Américas. Conversão em massa dos povos indígenas."},
    {"titulo": "Nossa Senhora da Medalha Milagrosa (Paris, 1830)", "status": "Reconhecida", "resumo": "Apareceu a Santa Catarina Labouré. Pediu a confecção da medalha com a inscrição “Ó Maria concebida sem pecado, rogai por nós que recorremos a vós”."},
    {"titulo": "Nossa Senhora de La Salette (França, 1846)", "status": "Reconhecida", "resumo": "Apareceu a dois pastorinhos chorando. Chamado forte à conversão e à oração."},
    {"titulo": "Nossa Senhora de Lourdes (França, 1858)", "status": "Reconhecida", "resumo": "18 aparições a Santa Bernadette Soubirous. “Eu sou a Imaculada Conceição”. Fonte de água e inúmeras curas. Um dos santuários mais visitados do mundo."},
    {"titulo": "Nossa Senhora de Fátima (Portugal, 1917)", "status": "Reconhecida", "resumo": "Apareceu aos três pastorinhos (Lúcia, Francisco e Jacinta). Pedidos de oração, penitência e consagração ao Imaculado Coração. Segredos e o milagre do sol."},
    {"titulo": "Nossa Senhora de Beauraing e Banneux (Bélgica, 1932-1933)", "status": "Reconhecida", "resumo": "Aparições a crianças. Virgem do Coração de Ouro e Virgem dos Pobres. Ênfase na oração e no amor aos sofredores."},
    {"titulo": "Nossa Senhora de Kibeho (Ruanda, 1981)", "status": "Reconhecida", "resumo": "Apareceu a jovens. Mensagens de conversão, oração e aviso sobre sofrimentos futuros (genocídio). Única aparição aprovada na África."},
    {"titulo": "Nossa Senhora Aparecida (Brasil, 1717)", "status": "Devoção oficial / Padroeira do Brasil", "resumo": "Não foi uma aparição visual clássica, mas o encontro milagroso da imagem no rio. Pio XI a proclamou Padroeira principal do Brasil em 1930. Maior santuário mariano do mundo em número de peregrinos."},
    {"titulo": "Nossa Senhora das Lágrimas (Campinas-SP, 1930)", "status": "Aprovação diocesana", "resumo": "Apareceu à Irmã Amália de Jesus Flagelado. Revelou a Coroa (Rosário) das Lágrimas. O bispo de Campinas reconheceu os fenômenos e autorizou a divulgação."},
    {"titulo": "Nossa Senhora das Graças de Cimbres (Pesqueira-PE, 1936)", "status": "Reconhecimento local", "resumo": "Apareceu a duas meninas (Maria da Luz e Maria da Conceição). Mensagens de conversão e proteção. Em 2021 a Diocese de Pesqueira reconheceu o caráter sobrenatural."},
    {"titulo": "Outras aparições aprovadas", "status": "Diversas", "resumo": "Pontmain (França, 1871), Knock (Irlanda, 1879), Akita (Japão, 1973), Champion (EUA), San Nicolás (Argentina) e outras receberam aprovação do bispo local ou reconhecimento mais amplo."},
]

# ============================================================
# FUNÇÕES DE INTERFACE
# ============================================================

def render_quiz(tema_id: str, quiz: List[Dict]):
    st.markdown('<div class="quiz-card">', unsafe_allow_html=True)
    st.markdown("#### ✅ Quiz – Teste seus conhecimentos")
    st.caption("Escolha a alternativa correta em cada pergunta.")
    
    score = 0
    respostas = {}
    
    for i, q in enumerate(quiz):
        key = f"{tema_id}_q{i}"
        resposta = st.radio(
            f"**{i+1}. {q['pergunta']}**",
            options=q["opcoes"],
            key=key,
            index=None
        )
        respostas[i] = resposta
    
    if st.button("Verificar respostas", key=f"btn_{tema_id}"):
        acertos = 0
        for i, q in enumerate(quiz):
            if respostas.get(i) == q["opcoes"][q["correta"]]:
                acertos += 1
                st.markdown(f'<div class="success-msg">✅ Pergunta {i+1}: Correta!</div>', unsafe_allow_html=True)
            else:
                correta = q["opcoes"][q["correta"]]
                st.markdown(f'<div class="error-msg">❌ Pergunta {i+1}: A resposta correta é “{correta}”</div>', unsafe_allow_html=True)
        
        st.markdown(f"### Resultado: {acertos} de {len(quiz)} acertos")
        if acertos == len(quiz):
            st.balloons()
            st.success("Parabéns! Você dominou este tema. Continue assim!")
        elif acertos >= 2:
            st.info("Muito bem! Revise o resumo para fixar ainda melhor.")
        else:
            st.warning("Que tal ler o resumo de novo e tentar outra vez?")
    
    st.markdown('</div>', unsafe_allow_html=True)


def render_tema_completo(tema: Dict, fase: str):
    with st.expander(f"📖 {tema['titulo']}", expanded=False):
        st.markdown(f'<div class="content-card">', unsafe_allow_html=True)
        st.markdown("##### Resumo para adolescentes")
        st.write(tema["resumo"])
        
        st.markdown('<div class="ref-box">', unsafe_allow_html=True)
        st.markdown(f"**📖 Bíblia (Edição Pastoral):** {tema['biblia']}")
        st.markdown(f"**📘 Catecismo da Igreja Católica:** {tema['catecismo']}")
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        render_quiz(f"{fase}_{tema['titulo'][:20]}", tema["quiz"])


def pagina_fases():
    st.title("✝️ Fases e Temas da Catequese")
    st.markdown("Conteúdos baseados na série *Crescer em Comunhão* (Vozes) e no Catecismo da Igreja Católica, adaptados para linguagem de adolescentes.")
    
    fase = st.selectbox(
        "Escolha a fase / etapa:",
        options=list(LISTA_FASES.keys()),
        index=0
    )
    
    st.markdown(f"### {fase}")
    
    # Temas com conteúdo completo
    completos = TEMAS_COMPLETOS.get(fase, [])
    titulos_completos = [t["titulo"] for t in completos]
    
    if completos:
        st.markdown("#### Temas com resumo + quiz completo")
        for tema in completos:
            render_tema_completo(tema, fase)
    
    # Lista de todos os temas da fase
    st.markdown("---")
    st.markdown("#### Todos os temas desta fase")
    st.caption("Os temas abaixo fazem parte do itinerário oficial. Os que possuem resumo completo estão destacados acima.")
    
    for i, tema_nome in enumerate(LISTA_FASES[fase], 1):
        # Verifica se tem versão completa
        tem_completo = any(tema_nome in t or t in tema_nome for t in titulos_completos)
        icon = "✅" if tem_completo else "📝"
        st.markdown(f"{icon} **{i}. {tema_nome}**")


def pagina_santos():
    st.title("🌟 Santos – Testemunhas de Cristo")
    st.markdown("Conheça santos do Brasil e do mundo que brilharam pela fé, caridade e coragem. Eles são nossos intercessores e modelos.")
    
    filtro = st.text_input("Buscar santo por nome ou país:", "")
    
    col1, col2 = st.columns(2)
    contador = 0
    for santo in SANTOS:
        if filtro.lower() in santo["nome"].lower() or filtro.lower() in santo["onde"].lower() or not filtro:
            with (col1 if contador % 2 == 0 else col2):
                st.markdown(f'''
                <div class="saint-card">
                    <strong>{santo["nome"]}</strong><br>
                    <small style="color:#64748b">{santo["onde"]}</small>
                    <p style="margin-top:0.5rem; font-size:0.95rem">{santo["resumo"]}</p>
                </div>
                ''', unsafe_allow_html=True)
            contador += 1
    
    st.caption(f"Total de santos apresentados: {len(SANTOS)}. A Igreja tem milhares de santos; estes são alguns dos mais significativos para nós.")


def pagina_milagres():
    st.title("✨ Milagres – Sinais do poder de Deus")
    st.markdown("Deus continua agindo na história. Estes são alguns dos milagres mais conhecidos e estudados.")
    
    for m in MILAGRES:
        st.markdown(f'''
        <div class="miracle-card">
            <strong>{m["titulo"]}</strong>
            <p style="margin-top:0.4rem">{m["resumo"]}</p>
        </div>
        ''', unsafe_allow_html=True)
    
    st.info("Os milagres não substituem a fé, mas a confirmam e nos convidam a louvar a Deus que é vivo e age.")


def pagina_aparicoes():
    st.title("🌹 Aparições de Nossa Senhora")
    st.markdown("Maria, mãe de Jesus e nossa mãe, continua visitando seus filhos. As aparições são revelações privadas: ajudam a viver o Evangelho, mas não acrescentam nada ao depósito da fé.")
    
    for a in APARICOES:
        st.markdown(f'''
        <div class="apparition-card">
            <strong>{a["titulo"]}</strong><br>
            <span style="background:#dbeafe; color:#1e40af; padding:2px 8px; border-radius:4px; font-size:0.8rem">{a["status"]}</span>
            <p style="margin-top:0.5rem">{a["resumo"]}</p>
        </div>
        ''', unsafe_allow_html=True)
    
    st.warning("A crença nas aparições, mesmo reconhecidas, não é obrigatória. O essencial continua sendo Jesus Cristo e o Evangelho.")


def pagina_sobre():
    st.title("ℹ️ Sobre este aplicativo")
    st.markdown("""
    **Catequese em Comunhão** é um material de apoio para catequizandos, catequistas e famílias.
    
    ### Fontes principais
    - Catecismo da Igreja Católica
    - Bíblia Edição Pastoral
    - Série *Crescer em Comunhão* (Editora Vozes)
    - Diretório para a Catequese (2020)
    - YouCat e materiais da CNBB
    
    ### Como usar
    1. Escolha a **fase** da catequese no menu.
    2. Abra os temas com resumo e faça o **quiz**.
    3. Explore as seções de **Santos**, **Milagres** e **Aparições**.
    
    ### Observações
    - Linguagem adaptada para adolescentes e jovens.
    - Não substitui o acompanhamento do catequista e da comunidade.
    - Conteúdo em constante enriquecimento.
    
    ---
    *“Na alegria de crer e comunicar a fé!”*  
    Arquidiocese de Sorocaba e paróquias irmãs.
    """)


# ============================================================
# MAIN
# ============================================================
def main():
    with st.sidebar:
        st.image("https://cdn-icons-png.flaticon.com/512/3312/3312680.png", width=80)
        st.markdown("## ✝️ Catequese em Comunhão")
        st.markdown("Formação para adolescentes e jovens")
        st.markdown("---")
        
        pagina = st.radio(
            "Navegação",
            options=[
                "🏠 Início",
                "📚 Fases e Temas",
                "🌟 Santos",
                "✨ Milagres",
                "🌹 Aparições de Maria",
                "ℹ️ Sobre"
            ],
            label_visibility="collapsed"
        )
        
        st.markdown("---")
        st.caption("Material de apoio catequético\nSem necessidade de login")
    
    if pagina == "🏠 Início":
        st.title("Bem-vindo(a) à Catequese em Comunhão!")
        st.markdown("""
        Este espaço foi feito para você **crescer na amizade com Jesus**, conhecer melhor a fé católica 
        e se preparar com alegria para os sacramentos.
        
        ### O que você encontra aqui:
        - **Fases e Temas** da catequese (Infantil, Eucaristia, Crisma, Adultos) com resumos claros e quizzes
        - **Santos** do Brasil e do mundo – modelos de vida
        - **Milagres** que mostram o poder de Deus
        - **Aparições de Nossa Senhora** reconhecidas pela Igreja
        
        Use o menu ao lado para navegar.  
        Que o Espírito Santo ilumine sua caminhada!
        """)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.info("📚 **Estude** os temas com calma")
        with col2:
            st.success("✅ **Faça** os quizzes para fixar")
        with col3:
            st.warning("🙏 **Reze** e viva o que aprendeu")
    
    elif pagina == "📚 Fases e Temas":
        pagina_fases()
    elif pagina == "🌟 Santos":
        pagina_santos()
    elif pagina == "✨ Milagres":
        pagina_milagres()
    elif pagina == "🌹 Aparições de Maria":
        pagina_aparicoes()
    elif pagina == "ℹ️ Sobre":
        pagina_sobre()


if __name__ == "__main__":
    main()
