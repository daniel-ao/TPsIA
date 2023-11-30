%% Introduction à l'IA - TD 2
%% Un système expert médical en Prolog
%%
%% Etape 1: Charger ce fichier dans SWI-Prolog
%%
%% Guide d utilisation des commandes SWI à utiliser dans votre terminal : https://www.swi-prolog.org/pldoc/man?section=cmdline
%% \!\: vous devez produire un exécutable de ce fichier pour pouvoir l utiliser
%%
%% Etape 2 : Exécuter le fichier en effectuant la requête
%% ?- consultation.
%% (répondre avec ";" à un diagnostic pour avoir le suivant.)
%% ?- effacer.
%% pour effectuer une autre consultation si on n'a pas vu tous les diagnostics.

:- dynamic positif/1.
:- dynamic negatif/1.

consultation :- writeln('Bienvenue au service de consultation automatique.'),
	writeln('Votre nom :'),
	%% Ici, votre nom est sauvegardé dans la variable "Name" qui va etre réutilisé à la fin de la consultation
	readln([Name | _]),
	%% TODO: Le système a besoin des connaissances pour pouvoir fonctionner, à vous de jouer !
	diagnostic(Dis),
	% !, % "ceci si on ne veut qu'un seul diagnostic et ensuite il faut effacer."
	%% Dans ce scénario, le systeme est capable de déterminer la cause
	write(Name), write(', votre diagnostic est : '), writeln(Dis).

%% Dans ce scénario, le systeme n est pas capable de déterminer la cause
consultation :- writeln('Desole, je n\'arrive pas a faire de diagnostic.'),
	effacer.

%% Le prédicat "symptome" prend en argument "X", nous allons donc appeler ce prédicat en donnant une valeur à X qui sera interpreté
symptome(X) :-
	%% On pose une question à l utilisateur en utilisant "X"
	atomic_list_concat(['Avez-vous', X, '? (oui/non)'], ' ', Q),
	%% La variable Q correspond à la réponse que l'on donne à cette question
	sym_positif(Q, X).

sym_positif(_, X) :- positif(X), !.
sym_positif(Q, X) :- not(negatif(X)),
	interroger(Q, X, R), R = [oui].

interroger(Q, X, R) :- writeln(Q), readln(R), enregistrer(X, R).

enregistrer(X, [oui]) :- asserta(positif(X)).
enregistrer(X, [non]) :- asserta(negatif(X)).

% On fait le ménage:
% la commande "retractall" permet d'effacer tous les renseignements (liste de "oui" et/ou de "non") que nous avons donné au système
effacer :-
	retractall(positif(_)),
	retractall(negatif(_)).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%% écrire ici la connaissance "experte" permettant de faire des diagnostics
%% sous forme de règles comme celle de cet exemple:
% Diseases with common symptoms
diagnostic(grippe) :-
    symptome('fièvre élevée'),
    symptome('fatigue extrême'),
    symptome('douleurs musculaires'),
    symptome('mal de tête'),
    symptome('toux sèche'),
    symptome('nez qui coule').

diagnostic(covid19) :-
    symptome('fièvre élevée'),
    symptome('fatigue extrême'),
    symptome('douleurs musculaires'),
    symptome('perte de goût ou d\'odorat'),
    symptome('toux sèche'),
    symptome('essoufflement').

diagnostic(rhume) :-
    symptome('fièvre légère'),
    symptome('nez qui coule'),
    symptome('mal à la gorge'),
    symptome('conjonctivite'),
    symptome('éternuements fréquents').

diagnostic(allergie_pollen) :-
    symptome('nez qui coule'),
    symptome('éternuements fréquents'),
    symptome('démangeaisons du nez'),
    symptome('conjonctivite').

diagnostic(sinusite) :-
    symptome('fièvre légère'),
    symptome('douleur faciale'),
    symptome('congestion nasale'),
    symptome('mal de tête').

diagnostic(otite) :-
    symptome('fièvre légère'),
    symptome('douleur d\'oreille'),
    symptome('écoulement d\'oreille').

diagnostic(angine) :-
    symptome('fièvre légère'),
    symptome('mal de gorge'),
    symptome('ganglions enflés'),
    symptome('difficulté à avaler').

diagnostic(pneumonie) :-
    symptome('fièvre élevée'),
    symptome('toux productive'),
    symptome('essoufflement').

diagnostic(amygdalite) :-
    symptome('fièvre légère'),
    symptome('mal de gorge'),
    symptome('difficulté à avaler').

diagnostic(tuberculose) :-
    symptome('fièvre légère'),
    symptome('toux persistante'),
    symptome('perte de poids').

diagnostic(hypertension_arterielle) :-
    symptome('hypertension artérielle'),
    symptome('maux de tête'),
    symptome('fatigue'),
    symptome('étourdissements').

diagnostic(asthme) :-
    symptome('essoufflement'),
    symptome('sifflements respiratoires'),
    symptome('toux sèche').

diagnostic(ulcere_estomac) :-
    symptome('brûlures d\'estomac'),
    symptome('sensation de plénitude'),
    symptome('perte de poids').

diagnostic(vertige) :-
    symptome('étourdissements'),
    symptome('nausées'),
    symptome('perte d\'équilibre').

diagnostic(arthrite) :-
    symptome('douleurs articulaires'),
    symptome('gonflement des articulations'),
    symptome('raideur matinale').

diagnostic(diabete) :-
    symptome('soif excessive'),
    symptome('miction fréquente'),
    symptome('fatigue').

diagnostic(migraine) :-
    symptome('maux de tête sévères'),
    symptome('sensibilité à la lumière'),
    symptome('nausées').

diagnostic(parkinson) :-
    symptome('tremblements'),
    symptome('rigidité musculaire'),
    symptome('lenteur des mouvements').

diagnostic(cancer_poumon) :-
    symptome('toux persistante'),
    symptome('essoufflement'),
    symptome('perte de poids').

% (No Common Symptoms)
		diagnostic(diabete) :-
		    symptome('soif excessive'),
		    symptome('miction fréquente'),
		    symptome('fatigue').

		diagnostic(migraine) :-
		    symptome('maux de tête sévères'),
		    symptome('sensibilité à la lumière'),
		    symptome('nausées').

		diagnostic(parkinson) :-
		    symptome('tremblements'),
		    symptome('rigidité musculaire'),
		    symptome('lenteur des mouvements').

		diagnostic(cancer_poumon) :-
		    symptome('toux persistante'),
		    symptome('essoufflement'),
		    symptome('perte de poids').

		diagnostic(ulcere_estomac) :-
		    symptome('brûlures d\'estomac'),
		    symptome('sensation de plénitude'),
		    symptome('perte de poids').

		diagnostic(vertige) :-
		    symptome('étourdissements'),
		    symptome('nausées'),
		    symptome('perte d\'équilibre').

		diagnostic(arthrite) :-
		    symptome('douleurs articulaires'),
		    symptome('gonflement des articulations'),
		    symptome('raideur matinale').

		diagnostic(alzheimer) :-
		    symptome('perte de mémoire'),
		    symptome('confusion'),
		    symptome('difficulté à accomplir des tâches quotidiennes').

		diagnostic(schizophrenie) :-
		    symptome('hallucinations'),
		    symptome('idées délirantes'),
		    symptome('troubles de la pensée').

		diagnostic(appendicite) :-
		    symptome('douleur abdominale droite'),
		    symptome('nausées'),
		    symptome('vomissements').

	diagnostic(inconnu) :-
	    writeln('Je ne peux pas déterminer la maladie avec les informations fournies.').
