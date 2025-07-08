#BIBLIOTECAS................................................................................
import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn import svm

# LIMPAR TELA (simulação)...................................................................
def limpar_tela_fake():
    print("\n" * 1)

#CLASSIFICADOR..............................................................................
df = pd.read_csv('medico_db_TotalemnteTratado.csv')

X = df[['IdMedico', 'tip_urgencia', 'tip_acomod', 'tipo_cirurgia']]
y = df['tecnica']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
clf = DecisionTreeClassifier(random_state=1)
clf2 = svm.SVC()

clf.fit(X_train, y_train)
clf2.fit(X_train, y_train)

#MENU.......................................................................................
def menu():
 print("\nDigite: ")
 print('   \n1 - Para Classificador com Árvore Decisão')
 print('   \n2 - Para Classificador com SVM')
 print('   \n3 - Para sair')

#ARVORE.....................................................................................
def menu_arvore():
  print('\n')
  print('='*50)
  print(" "*12,'ÁRVORE DE DECISÂO - MENU: ')
  print('='*50)
  print('   \n1 - Mostrar desempenho')
  print('   \n2 - Mostrar desenho da árvore')
  print('   \n3 - Fazer nova classificação')
  print('   \n4 - Voltar ao menu principal')

def desempenho_arvore():
 y_pred = clf.predict(X_test)
 acuracia = accuracy_score(y_test, y_pred)
 print('\n')
 print('~'*50)
 print(" "*14,">> Desempenho: {:.0f}% <<".format(acuracia*100))
 print('~'*50)

def desenho_arvore():
 data_colunas_uteis = ['IdMedico', 'tip_urgencia', 'tip_acomod', 'tipo_cirurgia']
 data_class_names = ['0','1']
 print('\n')
 print('='*50)
 print(" "*8,">> Desenho da Árvore de decisão <<")
 print('='*50)
 print('\n')
 tree.plot_tree(clf, feature_names = data_colunas_uteis,class_names= data_class_names, filled = True)
 plt.show()

def nova_classificacao():
 entrada_dicionario = {'IdMedico': int(input('\n>>Id Medico(1 até 721)\n')),
            'tip_urgencia': float(input('\n>>Tipo de Urgencia:\n0: não urgente \n1: urgente\n')),
            'tipo_cirurgia': int(input('\n>>Tipo de Cirugia:\n 0: Cirurgia oncológica,\n 1: Apendicectomia,\n 2: Colecistectomia,\n 3: Hérnia inguinal,\n 4: Lipoaspiração estética,\n 5: Cirurgia emergencial abdominal\n')),
            'tip_acomod': int(input('\n>>Tipo de acomodação:\n1:Acomodação Comum \n2: Acomodação de Emergencia\n')),
            }
 entrada = pd.DataFrame([entrada_dicionario],  columns=['IdMedico', 'tip_urgencia', 'tip_acomod', 'tipo_cirurgia'])
 pred = clf.predict(entrada)
 if pred == 1:
  print('\n')
  print('~'*50)
  print(" "*1,'>> Técnica usada: PADRÃO (cirurgia aberta) <<')
  print('~'*50)
 else:
  print('\n')
  print('~'*50)
  print(" "*3,'>> Técnica usada: VIDEOLAPAROSCOPIA <<')
  print('~'*50)

#SVM........................................................................................
def menu_svm():
  print('\n')
  print('='*50)
  print(" "*19,'SVM - MENU: ')
  print('='*50)
  print('   \n1 - Mostrar desempenho')
  print('   \n2 - Fazer nova classificação')
  print('   \n3 - Voltar ao menu principal')

def desempenho_svm():
 y_pred = clf2.predict(X_test)
 acuracia = accuracy_score(y_test, y_pred)
 print('\n')
 print('~'*50)
 print(" "*14,">> Desempenho: {:.0f}% <<".format(acuracia*100))
 print('~'*50)

def nova_classificacao_svm():
 entrada_dicionario = {'IdMedico': int(input('\n>>Id Medico(1 até 721)\n')),
            'tip_urgencia': float(input('\n>>Tipo de Urgencia:\n0: não urgente \n1: urgente\n')),
            'tipo_cirurgia': int(input('\n>>Tipo de Cirugia:\n 0: Cirurgia oncológica,\n 1: Apendicectomia,\n 2: Colecistectomia,\n 3: Hérnia inguinal,\n 4: Lipoaspiração estética,\n 5: Cirurgia emergencial abdominal\n')),
            'tip_acomod': int(input('\n>>Tipo de acomodação:\n1:Acomodação Comum \n2: Acomodação de Emergencia\n')),
            }
 entrada = pd.DataFrame([entrada_dicionario],  columns=['IdMedico', 'tip_urgencia', 'tip_acomod', 'tipo_cirurgia'])
 pred = clf2.predict(entrada)
 if pred == 1:
  print('\n')
  print('~'*50)
  print(" "*1,'>> Técnica usada: PADRÃO (cirurgia aberta) <<')
  print('~'*50)
 else:
  print('\n')
  print('~'*50)
  print(" "*3,'>> Técnica usada: VIDEOLAPAROSCOPIA <<')
  print('~'*50)

#ESCOLHAS...................................................................................
while True:
  print('\n')
  print('='*50)
  print('\n')
  print(" "*3,'>>> CLASSIFICADOR DE TÉCNICAS MÉDICAS <<<')
  print('\n')
  print('='*50)
  print('\n')
  menu()
  escolha = int(input('\n>> Escolha uma opção: '))
  if escolha == 1:
    while True:
     limpar_tela_fake()
     menu_arvore()
     escolha = int(input('\n>> Escolha uma opção: '))
     if escolha == 1:
      desempenho_arvore()
     elif escolha == 2:
      desenho_arvore()
     elif escolha == 3:
      nova_classificacao()
     elif escolha == 4:
      print('\n')
      print('\n>> Voltando ao menu principal...')
      break
  elif escolha == 2:
    while True:
      limpar_tela_fake()
      menu_svm()
      escolha_svm = int(input('\n>> Escolha uma opção: '))
      if escolha_svm == 1:
        desempenho_svm()
      elif escolha_svm == 2:
        nova_classificacao_svm()
      elif escolha_svm == 3:
        print('\n')
        print('\n>> Voltando ao menu principal...')
        break
  elif escolha == 3:
    print('='*50)
    print(" "*4,'Saindo... Obrigado por utilizar o sistema!')
    print('='*50)
    break
  else:
    print('\nOpção inválida, digite 1, 2 ou 3')
