# 🐾 GroqCLI ✨

Un outil de ligne de commande modernisé pour parler avec les LLMs de Groq, avec style femboy kawaii~ 💅💖

## 🌟 Fonctionnalités

- 🔮 Prompt direct ou via fichier avec rôles `[SYSTEM]`, `[USER]`, `[ASSISTANT]`
- 🌈 UI riche avec `rich` (couleurs, emojis, markdown, etc.)
- 🔁 Historique auto (3 dernières sessions) + sauvegarde manuelle avec `--save`
- 📂 Chargement de conversations précédentes avec `resume`
- 🧠 Prompts système prédéfinis avec `--system`, modifiables avec `prompts edit`
- 📜 Liste des modèles disponibles avec `models`
- 🧩 Entièrement extensible et installable via `pip` ou `pipx`

## 💻 Installation

```bash
# en local
pip install .

# ou via pipx pour utilisation globale
pipx install .
```

## 🧪 Utilisation

```bash
# prompt direct
$ groqcli "Explique moi les trous noirs en 3 points"

# depuis un fichier avec rôles
$ groqcli mon_fichier.txt

# avec un system prompt prédéfini
$ groqcli "Transforme ce script en TypeScript" --system formatScript

# recharger une session
$ groqcli resume --last 1
```

## 🎀 Exemple de fichier

```txt
[SYSTEM]
Tu es un assistant très poli, concis et structuré.

[USER]
Explique-moi le fonctionnement d’un moteur à explosion.
```

## ✨ Contribuer

Tu veux ajouter un thème dark, un TUI, ou une voix cute ? Fais une PR ou glisse-moi une idée 🥺👉👈

---

Meow merci d’utiliser GroqCLI 💖 UwU