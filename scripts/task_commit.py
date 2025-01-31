import subprocess
import re

def color_text(text, color):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "magenta": "\033[95m",
        "cyan": "\033[96m",
        "reset": "\033[0m"
    }
    return f"{colors.get(color, colors['reset'])}{text}{colors['reset']}"

def get_git_user():
    """Obtém o nome de usuário configurado no Git."""
    try:
        username = subprocess.check_output(["git", "config", "user.name"], text=True).strip()
        if not username:
            raise ValueError("Nome de usuário não configurado")
        return username
    except subprocess.CalledProcessError:
        return None
    except ValueError:
        return None

def add_user_to_commit(commit_msg, git_user):
    """Adiciona o nome do usuário à mensagem de commit."""
    return f"{commit_msg} (👤 Usuário: {git_user})"

def commit():
    """Commita as mudanças no Git utilizando Conventional Commits."""
    print(color_text("\n🚀 Iniciando processo de commit 🚀\n", "cyan"))
    add_all = input(color_text("📌 Deseja adicionar todas as mudanças? (✅ s / ❌ n) [s]: ", "yellow")).strip().lower() or "s"
    if add_all == 's':
        subprocess.run(["git", "add", "."])
    
    commit_type = input(color_text("🎯 Escolha o tipo de commit (feat, fix, chore, refactor, test, docs, style, ci, perf): ", "blue")).strip().lower()
    if commit_type not in ["feat", "fix", "chore", "refactor", "test", "docs", "style", "ci", "perf"]:
        print(color_text("❌ Tipo de commit inválido!", "red"))
        return
    
    module = input(color_text("🗂️ Qual módulo foi alterado? (exemplo: core, api, models): ", "magenta")).strip().lower()
    
    commit_message = input(color_text("📝 Digite a mensagem do commit: ", "green")).strip()
    if not commit_message:
        print(color_text("❌ Mensagem de commit é obrigatória!", "red"))
        return
    
    
    git_user = get_git_user()
    if git_user is None:
        print(color_text("❌ Erro: Nome de usuário do Git não configurado!", "red"))
        print(color_text("Por favor, configure seu nome de usuário no Git usando os seguintes comandos:", "yellow"))
        print(color_text("\ngit config --global user.name 'Seu Nome'", "cyan"))
        print(color_text("git config --global user.email 'seu.email@dominio.com'", "cyan"))
        return
    
    full_commit_message = f"{commit_type}({module}): {commit_message}"
    updated_commit_message = add_user_to_commit(full_commit_message, git_user)
    
    subprocess.run(["git", "commit", "-m", updated_commit_message])
    print(color_text("✅ Commit realizado com sucesso!\n", "green"))
    
    push = input(color_text("🚀 Deseja fazer push para o repositório? (✅ s / ❌ n) [s]: ", "yellow")).strip().lower() or "s"
    if push == 's':
        branch = input(color_text("🌿 Para qual branch deseja fazer push? [main]: ", "blue")).strip() or "main"
        subprocess.run(["git", "push", "origin", branch])
        print(color_text(f"✅ Push realizado para a branch {branch}!\n", "green"))

if __name__ == "__main__":
    commit()
