<!DOCTYPE html>
<html lang="pt-BR" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>FitPulse Pro - Treino, Nutrição & Guia Visual</title>

  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>
  <!-- Font Awesome 6 -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  <!-- Google Fonts: Plus Jakarta Sans -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">

  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          fontFamily: {
            sans: ['"Plus Jakarta Sans"', 'sans-serif'],
          },
          colors: {
            brand: {
              push: '#f43f5e',
              pull: '#0284c7',
              legs: '#10b981',
              dark: '#0a0e17',
              card: '#111827',
              border: '#1f293d'
            }
          }
        }
      }
    }
  </script>

  <style>
    body {
      background-color: #080c14;
      color: #f1f5f9;
      font-family: 'Plus Jakarta Sans', sans-serif;
      -webkit-tap-highlight-color: transparent;
    }
    .custom-scroll::-webkit-scrollbar {
      width: 5px;
      height: 5px;
    }
    .custom-scroll::-webkit-scrollbar-thumb {
      background: #334155;
      border-radius: 9999px;
    }
    .active-nav-btn {
      color: #38bdf8 !important;
      font-weight: 700;
    }
  </style>
</head>
<body class="min-h-screen pb-24 text-slate-100 antialiased selection:bg-cyan-500 selection:text-white">

  <header class="sticky top-0 z-40 bg-[#0c121e]/95 backdrop-blur-md border-b border-slate-800 px-4 py-3">
    <div class="max-w-lg mx-auto flex items-center justify-between gap-3">
      <div class="flex items-center gap-2.5">
        <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-cyan-500 via-blue-600 to-indigo-600 flex items-center justify-center font-extrabold text-white text-base shadow-lg shadow-cyan-500/20">
          FP
        </div>
        <div>
          <div class="flex items-center gap-1.5">
            <h1 class="text-base font-extrabold text-white tracking-tight leading-tight">FitPulse Pro</h1>
            <span class="text-[9px] bg-emerald-500/20 text-emerald-400 font-bold px-1.5 py-0.5 rounded border border-emerald-500/30">78kg • 1,86m</span>
          </div>
          <p class="text-[11px] font-medium text-slate-400">Hipertrofia Modular + Corrida/Basquete</p>
        </div>
      </div>

      <!-- Live kcal badge -->
      <div class="flex items-center gap-1 bg-slate-900 border border-slate-700/80 rounded-full px-3 py-1 text-xs">
        <i class="fa-solid fa-fire text-amber-400"></i>
        <span class="font-bold text-slate-200">3.000 kcal</span>
      </div>
    </div>
  </header>

  <main class="max-w-lg mx-auto px-4 pt-4 space-y-4">

    <!-- ========================================== -->
    <!-- TAB 1: WORKOUTS (TREINOS P/P/L) -->
    <!-- ========================================== -->
    <section id="tab-workouts" class="space-y-4">

      <!-- Routine Switcher Header -->
      <div class="bg-gradient-to-br from-slate-900 via-slate-900 to-slate-950 border border-slate-800 rounded-2xl p-4 shadow-xl relative overflow-hidden">
        <div class="flex justify-between items-start mb-2">
          <div>
            <span class="text-[10px] font-extrabold uppercase tracking-widest text-cyan-400">Divisão Semanal Modular</span>
            <h2 class="text-lg font-black text-white">Escolha o Treino de Hoje</h2>
          </div>
          <span class="text-[11px] bg-slate-800 text-slate-300 px-2 py-0.5 rounded-lg border border-slate-700 font-semibold">
            3 a 6x/sem
          </span>
        </div>
        <p class="text-xs text-slate-300 mb-3">
          Toque em qualquer exercício para abrir a visualização anatômica completa ou trocar a foto por uma sua.
        </p>

        <!-- Selector buttons -->
        <div class="grid grid-cols-3 gap-2">
          <button onclick="setWorkout('push')" id="btn-push" class="flex flex-col items-center justify-center py-2.5 px-2 rounded-xl border border-rose-500/50 bg-rose-950/40 text-rose-400 font-bold text-xs transition active:scale-95 shadow-lg shadow-rose-950/20">
            <i class="fa-solid fa-dumbbell mb-1 text-sm"></i>
            <span>Treino A</span>
            <span class="text-[10px] font-normal opacity-80">Push (5)</span>
          </button>
          <button onclick="setWorkout('pull')" id="btn-pull" class="flex flex-col items-center justify-center py-2.5 px-2 rounded-xl border border-slate-800 bg-slate-900 text-slate-400 font-semibold text-xs transition active:scale-95">
            <i class="fa-solid fa-hand-back-fist mb-1 text-sm"></i>
            <span>Treino B</span>
            <span class="text-[10px] font-normal opacity-80">Pull (4)</span>
          </button>
          <button onclick="setWorkout('legs')" id="btn-legs" class="flex flex-col items-center justify-center py-2.5 px-2 rounded-xl border border-slate-800 bg-slate-900 text-slate-400 font-semibold text-xs transition active:scale-95">
            <i class="fa-solid fa-shoe-prints mb-1 text-sm"></i>
            <span>Treino C</span>
            <span class="text-[10px] font-normal opacity-80">Legs (5)</span>
          </button>
        </div>
      </div>

      <!-- Quick Action: Running & Basketball advice -->
      <div class="grid grid-cols-2 gap-2">
        <button onclick="openInfoModal('corrida')" class="bg-slate-900 border border-slate-800 hover:border-amber-500/40 p-2.5 rounded-xl flex items-center gap-2.5 text-left transition active:scale-95">
          <div class="w-8 h-8 rounded-lg bg-amber-500/20 text-amber-400 flex items-center justify-center text-sm font-bold flex-shrink-0">
            <i class="fa-solid fa-person-running"></i>
          </div>
          <div>
            <div class="text-xs font-bold text-white">Corrida Z2</div>
            <div class="text-[10px] text-slate-400">Cardio sem queimar massa</div>
          </div>
        </button>
        <button onclick="openInfoModal('basquete')" class="bg-slate-900 border border-slate-800 hover:border-orange-500/40 p-2.5 rounded-xl flex items-center gap-2.5 text-left transition active:scale-95">
          <div class="w-8 h-8 rounded-lg bg-orange-500/20 text-orange-400 flex items-center justify-center text-sm font-bold flex-shrink-0">
            <i class="fa-solid fa-basketball"></i>
          </div>
          <div>
            <div class="text-xs font-bold text-white">Basquete</div>
            <div class="text-[10px] text-slate-400">Gestão de pernas</div>
          </div>
        </button>
      </div>

      <!-- Rest stopwatch timer -->
      <div class="bg-slate-900/90 border border-slate-800 rounded-xl p-3 flex items-center justify-between shadow-inner">
        <div class="flex items-center gap-2">
          <div class="w-8 h-8 rounded-lg bg-cyan-500/10 text-cyan-400 flex items-center justify-center text-sm">
            <i class="fa-solid fa-stopwatch"></i>
          </div>
          <div>
            <span class="text-[10px] uppercase font-bold text-slate-400 block -mb-0.5">Descanso Entre Séries</span>
            <span id="timer-text" class="font-mono text-base font-black text-cyan-300">00:00</span>
          </div>
        </div>
        <div class="flex items-center gap-1.5">
          <button onclick="startRest(60)" class="text-xs bg-slate-800 hover:bg-cyan-600 px-2.5 py-1.5 rounded-lg text-slate-200 font-semibold transition active:scale-95">60s</button>
          <button onclick="startRest(90)" class="text-xs bg-slate-800 hover:bg-cyan-600 px-2.5 py-1.5 rounded-lg text-slate-200 font-semibold transition active:scale-95">90s</button>
          <button onclick="startRest(120)" class="text-xs bg-slate-800 hover:bg-cyan-600 px-2.5 py-1.5 rounded-lg text-slate-200 font-semibold transition active:scale-95">120s</button>
          <button onclick="stopRest()" class="text-xs text-rose-400 hover:text-rose-300 p-1.5" title="Parar"><i class="fa-solid fa-circle-stop"></i></button>
        </div>
      </div>

      <!-- Exercises List Container -->
      <div class="flex justify-between items-center px-1">
        <h3 id="workout-label" class="text-sm font-bold text-white">Treino A — Push</h3>
        <span id="workout-stats-badge" class="text-xs text-slate-400 font-medium">5 exercícios</span>
      </div>

      <!-- GitHub Folder Notice Card -->
      <div class="bg-gradient-to-r from-blue-950/40 via-indigo-950/30 to-slate-900 border border-blue-500/30 rounded-xl p-3 text-xs flex flex-col gap-2">
        <div class="flex items-start justify-between gap-2">
          <div class="flex items-start gap-2.5">
            <div class="w-7 h-7 rounded-lg bg-blue-500/20 text-blue-400 flex items-center justify-center flex-shrink-0 mt-0.5">
              <i class="fa-solid fa-images text-xs"></i>
            </div>
            <div class="text-[11px] leading-relaxed text-slate-300">
              <span class="font-bold text-white block mb-0.5">Pasta <code class="text-cyan-300 bg-slate-950 px-1 py-0.5 rounded border border-slate-800">imagens/</code> (.PNG)</span>
              O app busca arquivos <code class="text-cyan-300 font-bold">.png</code> (com e sem acento/espaço).
            </div>
          </div>
          <!-- Diagnostic trigger -->
          <button onclick="openDiagnosticModal()" class="px-2.5 py-1 rounded-lg bg-cyan-600/30 hover:bg-cyan-600 text-cyan-300 hover:text-white border border-cyan-500/40 text-[11px] font-bold transition flex items-center gap-1.5 flex-shrink-0 active:scale-95">
            <i class="fa-solid fa-stethoscope text-[10px]"></i>
            <span>Testar Links</span>
          </button>
        </div>
      </div>

      <div id="exercises-container" class="space-y-3.5">
        <!-- Rendered dynamically via JavaScript -->
      </div>
    </section>

    <!-- ========================================== -->
    <!-- TAB 2: NUTRITION (ALIMENTAÇÃO ~3.000 KCAL) -->
    <!-- ========================================== -->
    <section id="tab-nutrition" class="space-y-4 hidden">
      <!-- Target Calories Card -->
      <div class="bg-gradient-to-br from-slate-900 via-slate-900 to-indigo-950/50 border border-purple-500/30 rounded-2xl p-4 shadow-xl">
        <div class="flex justify-between items-start mb-3">
          <div>
            <span class="text-[10px] font-extrabold uppercase tracking-widest text-purple-400">Meta Diária • Bulking Limpo</span>
            <h2 class="text-2xl font-black text-white">3.000 <span class="text-xs font-medium text-slate-400">kcal/dia</span></h2>
          </div>
          <div class="text-right">
            <span class="text-xs font-semibold text-slate-300">Perfil: 78kg • 1,86m</span>
            <div class="text-[11px] text-emerald-400 font-semibold">+250 kcal superávit</div>
          </div>
        </div>

        <div class="grid grid-cols-3 gap-2 pt-2 border-t border-slate-800 text-center">
          <div class="bg-slate-850 bg-slate-900/80 p-2.5 rounded-xl border border-slate-700/60">
            <div class="text-[11px] font-bold text-blue-400">Proteína</div>
            <div class="text-base font-black text-white">160g</div>
            <div class="text-[10px] text-slate-400">~640 kcal (2.0g/kg)</div>
          </div>
          <div class="bg-slate-850 bg-slate-900/80 p-2.5 rounded-xl border border-slate-700/60">
            <div class="text-[11px] font-bold text-amber-400">Carboidrato</div>
            <div class="text-base font-black text-white">400g</div>
            <div class="text-[10px] text-slate-400">~1.600 kcal</div>
          </div>
          <div class="bg-slate-850 bg-slate-900/80 p-2.5 rounded-xl border border-slate-700/60">
            <div class="text-[11px] font-bold text-rose-400">Gorduras</div>
            <div class="text-base font-black text-white">85g</div>
            <div class="text-[10px] text-slate-400">~765 kcal</div>
          </div>
        </div>
      </div>

      <!-- Visual Hand Portion Guide -->
      <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4">
        <h3 class="text-sm font-bold text-white mb-2.5 flex items-center gap-2">
          <i class="fa-solid fa-hand text-purple-400"></i>
          Guia Prático da Mão (Sem Balança)
        </h3>
        <div class="grid grid-cols-2 gap-2 text-xs">
          <div class="bg-slate-800/40 p-2.5 rounded-xl border border-slate-800 flex items-center gap-2.5">
            <div class="w-8 h-8 rounded-lg bg-blue-500/20 text-blue-400 flex items-center justify-center font-bold text-sm">
              <i class="fa-solid fa-hand-back-fist"></i>
            </div>
            <div>
              <div class="font-bold text-slate-200">1 Punho Fechado</div>
              <div class="text-[11px] text-slate-400">~100g Arroz ou Batata</div>
            </div>
          </div>
          <div class="bg-slate-800/40 p-2.5 rounded-xl border border-slate-800 flex items-center gap-2.5">
            <div class="w-8 h-8 rounded-lg bg-emerald-500/20 text-emerald-400 flex items-center justify-center font-bold text-sm">
              <i class="fa-solid fa-hand"></i>
            </div>
            <div>
              <div class="font-bold text-slate-200">1 Palma da Mão</div>
              <div class="text-[11px] text-slate-400">~120-150g Frango ou Ovos</div>
            </div>
          </div>
          <div class="bg-slate-800/40 p-2.5 rounded-xl border border-slate-800 flex items-center gap-2.5">
            <div class="w-8 h-8 rounded-lg bg-rose-500/20 text-rose-400 flex items-center justify-center font-bold text-sm">
              <i class="fa-solid fa-thumbs-up"></i>
            </div>
            <div>
              <div class="font-bold text-slate-200">1 Polegar</div>
              <div class="text-[11px] text-slate-400">~15g Azeite / Pasta Amendoim</div>
            </div>
          </div>
          <div class="bg-slate-800/40 p-2.5 rounded-xl border border-slate-800 flex items-center gap-2.5">
            <div class="w-8 h-8 rounded-lg bg-amber-500/20 text-amber-400 flex items-center justify-center font-bold text-sm">
              <i class="fa-solid fa-hand-holding"></i>
            </div>
            <div>
              <div class="font-bold text-slate-200">2 Mãos em Concha</div>
              <div class="text-[11px] text-slate-400">Vegetais e Saladas livres</div>
            </div>
          </div>
        </div>
      </div>

      <!-- Water Tracker -->
      <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4">
        <div class="flex justify-between items-center mb-2">
          <div class="flex items-center gap-2">
            <i class="fa-solid fa-droplet text-cyan-400"></i>
            <span class="text-sm font-bold text-white">Hidratação (Meta: 3.500 ml)</span>
          </div>
          <span id="water-text" class="text-xs font-bold text-cyan-400">0 / 3.500 ml</span>
        </div>
        <div class="w-full bg-slate-800 rounded-full h-2.5 mb-3 overflow-hidden">
          <div id="water-bar" class="bg-cyan-500 h-2.5 rounded-full transition-all duration-300" style="width: 0%"></div>
        </div>
        <div class="flex gap-2">
          <button onclick="addWater(250)" class="flex-1 bg-slate-800 hover:bg-slate-700 py-2 rounded-xl text-xs font-bold text-slate-200 transition active:scale-95 flex items-center justify-center gap-1.5">
            <i class="fa-solid fa-glass-water text-cyan-400"></i> +250 ml
          </button>
          <button onclick="addWater(500)" class="flex-1 bg-slate-800 hover:bg-slate-700 py-2 rounded-xl text-xs font-bold text-slate-200 transition active:scale-95 flex items-center justify-center gap-1.5">
            <i class="fa-solid fa-bottle-water text-cyan-400"></i> +500 ml
          </button>
          <button onclick="resetWater()" class="px-3 bg-slate-800 hover:bg-rose-950/40 text-rose-400 py-2 rounded-xl text-xs font-bold transition">
            Zerar
          </button>
        </div>
      </div>

      <!-- Meals checklist -->
      <div class="space-y-2.5">
        <div class="flex justify-between items-center px-1">
          <h3 class="text-sm font-bold text-white">Refeições Estruturadas</h3>
          <span class="text-[11px] text-slate-400">Marque ao cumprir</span>
        </div>

        <div class="bg-slate-900 border border-slate-800 rounded-xl p-3.5 flex items-start gap-3">
          <input type="checkbox" id="chk-meal-1" onchange="toggleMealCheck(1, this.checked)" class="mt-1 w-5 h-5 rounded accent-purple-500 cursor-pointer">
          <label for="chk-meal-1" class="flex-1 cursor-pointer">
            <div class="flex justify-between items-center">
              <span class="text-xs font-bold text-white">1. Café da Manhã Energético</span>
              <span class="text-xs font-semibold text-purple-400">~600 kcal</span>
            </div>
            <p class="text-[11px] text-slate-300 mt-1">3 ovos mexidos + 2 fatias de pão integral + 1 banana com 30g de aveia e fio de mel.</p>
            <div class="text-[10px] text-slate-500 mt-1 font-medium">30g Proteína • 70g Carboidrato</div>
          </label>
        </div>

        <div class="bg-slate-900 border border-slate-800 rounded-xl p-3.5 flex items-start gap-3">
          <input type="checkbox" id="chk-meal-2" onchange="toggleMealCheck(2, this.checked)" class="mt-1 w-5 h-5 rounded accent-purple-500 cursor-pointer">
          <label for="chk-meal-2" class="flex-1 cursor-pointer">
            <div class="flex justify-between items-center">
              <span class="text-xs font-bold text-white">2. Almoço Completo</span>
              <span class="text-xs font-semibold text-purple-400">~850 kcal</span>
            </div>
            <p class="text-[11px] text-slate-300 mt-1">6 colheres cheias de arroz (180g) + 1 concha de feijão (100g) + 180g de carne ou frango grelhado + salada com azeite.</p>
            <div class="text-[10px] text-slate-500 mt-1 font-medium">45g Proteína • 105g Carboidrato</div>
          </label>
        </div>

        <div class="bg-slate-900 border border-slate-800 rounded-xl p-3.5 flex items-start gap-3">
          <input type="checkbox" id="chk-meal-3" onchange="toggleMealCheck(3, this.checked)" class="mt-1 w-5 h-5 rounded accent-purple-500 cursor-pointer">
          <label for="chk-meal-3" class="flex-1 cursor-pointer">
            <div class="flex justify-between items-center">
              <span class="text-xs font-bold text-white">3. Shake Pré/Pós-Treino</span>
              <span class="text-xs font-semibold text-purple-400">~450 kcal</span>
            </div>
            <p class="text-[11px] text-slate-300 mt-1">1 scoop Whey Protein (30g) batido com 200ml leite + 1 banana grande + 30g de pasta de amendoim ou aveia.</p>
            <div class="text-[10px] text-slate-500 mt-1 font-medium">35g Proteína • 45g Carboidrato</div>
          </label>
        </div>

        <div class="bg-slate-900 border border-slate-800 rounded-xl p-3.5 flex items-start gap-3">
          <input type="checkbox" id="chk-meal-4" onchange="toggleMealCheck(4, this.checked)" class="mt-1 w-5 h-5 rounded accent-purple-500 cursor-pointer">
          <label for="chk-meal-4" class="flex-1 cursor-pointer">
            <div class="flex justify-between items-center">
              <span class="text-xs font-bold text-white">4. Jantar de Recuperação</span>
              <span class="text-xs font-semibold text-purple-400">~800 kcal</span>
            </div>
            <p class="text-[11px] text-slate-300 mt-1">200g batata inglesa ou arroz cozido + 180g peito de frango ou patinho moído + legumes cozidos.</p>
            <div class="text-[10px] text-slate-500 mt-1 font-medium">42g Proteína • 95g Carboidrato</div>
          </label>
        </div>

        <div class="bg-slate-900 border border-slate-800 rounded-xl p-3.5 flex items-start gap-3">
          <input type="checkbox" id="chk-meal-5" onchange="toggleMealCheck(5, this.checked)" class="mt-1 w-5 h-5 rounded accent-purple-500 cursor-pointer">
          <label for="chk-meal-5" class="flex-1 cursor-pointer">
            <div class="flex justify-between items-center">
              <span class="text-xs font-bold text-white">5. Ceia Noturna Anabólica</span>
              <span class="text-xs font-semibold text-purple-400">~300 kcal</span>
            </div>
            <p class="text-[11px] text-slate-300 mt-1">1 pote de iogurte natural com 20g de castanhas e 1 maçã fatiada.</p>
            <div class="text-[10px] text-slate-500 mt-1 font-medium">15g Proteína • 25g Carboidrato</div>
          </label>
        </div>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- TAB 3: VISUAL GUIDE GALLERY -->
    <!-- ========================================== -->
    <section id="tab-gallery" class="space-y-4 hidden">
      <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 shadow-xl">
        <h3 class="text-sm font-bold text-white mb-1">Catálogo Visual Completo de Movimentos</h3>
        <p class="text-xs text-slate-400 mb-3">
          Todos os exercícios com foto nítida e anatomia. Você pode clicar para ver o passo a passo ou carregar sua própria imagem personalizada para qualquer um deles.
        </p>

        <div class="flex gap-2 overflow-x-auto pb-2 custom-scroll mb-3">
          <button onclick="filterGallery('all')" class="gallery-filter-btn px-3 py-1 rounded-lg text-xs font-bold bg-cyan-600 text-white flex-shrink-0">Todos</button>
          <button onclick="filterGallery('push')" class="gallery-filter-btn px-3 py-1 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 flex-shrink-0">Push</button>
          <button onclick="filterGallery('pull')" class="gallery-filter-btn px-3 py-1 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 flex-shrink-0">Pull</button>
          <button onclick="filterGallery('legs')" class="gallery-filter-btn px-3 py-1 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 flex-shrink-0">Legs</button>
        </div>

        <div id="gallery-grid" class="grid grid-cols-2 gap-3">
          <!-- Rendered dynamically -->
        </div>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- TAB 4: PROGRESS & LOGS -->
    <!-- ========================================== -->
    <section id="tab-progress" class="space-y-4 hidden">
      <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 shadow-xl">
        <h3 class="text-sm font-bold text-white mb-1">Evolução Semanal de Peso (Jejum)</h3>
        <p class="text-xs text-slate-400 mb-4">Ganho limpo projetado: 250g a 400g/semana (~1kg a 1,5kg por mês) para preservar definição muscular.</p>

        <div class="grid grid-cols-2 gap-2.5 mb-4">
          <div class="bg-slate-800/80 p-3 rounded-xl border border-slate-700/60">
            <span class="text-[10px] text-slate-400 block font-semibold uppercase">Peso Inicial</span>
            <span class="text-xl font-black text-white">78.0 kg</span>
          </div>
          <div class="bg-slate-800/80 p-3 rounded-xl border border-emerald-500/40">
            <span class="text-[10px] text-emerald-400 block font-semibold uppercase">Meta Atual</span>
            <span class="text-xl font-black text-emerald-400">82.0 kg</span>
          </div>
        </div>

        <div class="bg-slate-950 p-3.5 rounded-xl border border-slate-800">
          <div class="flex justify-between items-center mb-2.5">
            <span class="text-xs font-bold text-slate-200">Registros Recentes</span>
            <button onclick="promptNewWeight()" class="text-xs text-cyan-400 hover:text-cyan-300 font-bold flex items-center gap-1">
              <i class="fa-solid fa-plus text-[10px]"></i> Novo Peso
            </button>
          </div>
          <ul id="weight-history-list" class="text-xs space-y-2 divide-y divide-slate-800/70 text-slate-300">
            <!-- Dynamic entries -->
          </ul>
        </div>
      </div>

      <!-- Functional Exercises Box -->
      <div class="bg-slate-900 border border-slate-800 rounded-2xl p-4">
        <h4 class="text-xs font-bold text-white uppercase tracking-wider mb-2 flex items-center gap-2">
          <i class="fa-solid fa-shield-halved text-emerald-400"></i> Proteção Articular & Basquete
        </h4>
        <div class="grid grid-cols-2 gap-2 text-xs">
          <div onclick="openExerciseModal('wall_sit')" class="bg-slate-850 bg-slate-800/50 p-3 rounded-xl border border-slate-700/60 cursor-pointer hover:border-cyan-500 transition">
            <div class="font-bold text-white mb-0.5">Wall Sit (Parede)</div>
            <div class="text-[10px] text-cyan-400">Isometria para Tendão Patelar</div>
          </div>
          <div onclick="openExerciseModal('step_up')" class="bg-slate-850 bg-slate-800/50 p-3 rounded-xl border border-slate-700/60 cursor-pointer hover:border-cyan-500 transition">
            <div class="font-bold text-white mb-0.5">Step-up na Caixa</div>
            <div class="text-[10px] text-emerald-400">Pliometria e Salto Vertical</div>
          </div>
        </div>
      </div>
    </section>

  </main>

  <!-- ========================================== -->
  <!-- MODAL: DETAILED EXERCISE VIEW & UPLOAD -->
  <!-- ========================================== -->
  <div id="exercise-modal" class="fixed inset-0 z-50 bg-black/90 backdrop-blur-md flex items-end sm:items-center justify-center p-0 sm:p-4 hidden">
    <div class="bg-slate-900 border border-slate-800 w-full max-w-lg rounded-t-3xl sm:rounded-2xl p-5 max-h-[92vh] overflow-y-auto custom-scroll">
      
      <!-- Modal Header -->
      <div class="flex justify-between items-start mb-3">
        <div>
          <span id="modal-category" class="text-[10px] font-extrabold uppercase tracking-widest text-cyan-400">Treino Push</span>
          <h3 id="modal-title" class="text-lg font-black text-white leading-tight">Supino Reto</h3>
        </div>
        <button onclick="closeExerciseModal()" class="w-8 h-8 rounded-full bg-slate-800 text-slate-400 hover:text-white flex items-center justify-center transition">
          <i class="fa-solid fa-xmark"></i>
        </button>
      </div>

      <!-- Real Image Presentation Box with Reliable Fallback -->
      <div class="w-full bg-slate-950 rounded-2xl mb-3.5 border border-slate-800 overflow-hidden relative group p-2 flex items-center justify-center min-h-[220px]">
        <img id="modal-image" src="" alt="Exercício" class="w-full max-h-72 object-contain rounded-xl transition-all duration-300" onerror="handleImageError(this)">
        <div class="absolute bottom-3 right-3 bg-black/80 backdrop-blur-md text-[10px] font-bold text-white px-2.5 py-1 rounded-md border border-white/10 flex items-center gap-1.5">
          <i class="fa-solid fa-check text-emerald-400"></i> Guia Verificado
        </div>
      </div>

      <!-- Custom Photo Upload for this specific exercise -->
      <div class="mb-4 bg-slate-950/70 p-3 rounded-xl border border-slate-800 flex items-center justify-between gap-2">
        <div class="flex items-center gap-2">
          <i class="fa-solid fa-camera text-cyan-400 text-sm"></i>
          <div>
            <div class="text-xs font-bold text-white">Sua própria foto</div>
            <div class="text-[10px] text-slate-400">Substitua a imagem por uma foto sua</div>
          </div>
        </div>
        <label class="cursor-pointer bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-bold px-3 py-1.5 rounded-lg border border-slate-700 transition active:scale-95">
          <span>Escolher Foto</span>
          <input type="file" id="modal-file-input" accept="image/*" class="hidden" onchange="handleUserPhotoUpload(event)">
        </label>
      </div>

      <!-- Content Specs -->
      <div class="space-y-3.5 text-xs">
        <div>
          <h4 class="font-bold text-slate-300 mb-1.5 flex items-center gap-1.5">
            <i class="fa-solid fa-crosshairs text-cyan-400"></i> Músculos Trabalhados:
          </h4>
          <div id="modal-muscles" class="flex flex-wrap gap-1.5">
            <!-- Dynamic muscle badges -->
          </div>
        </div>

        <div>
          <h4 class="font-bold text-slate-300 mb-1.5 flex items-center gap-1.5">
            <i class="fa-solid fa-list-check text-cyan-400"></i> Execução Passo a Passo:
          </h4>
          <ol id="modal-steps" class="list-decimal list-inside space-y-1.5 text-slate-300 leading-relaxed bg-slate-950/80 p-3.5 rounded-xl border border-slate-800">
            <!-- Dynamic steps -->
          </ol>
        </div>

        <div class="bg-amber-950/30 border border-amber-500/40 p-3 rounded-xl text-amber-200">
          <div class="font-bold mb-0.5 flex items-center gap-1.5 text-amber-400">
            <i class="fa-solid fa-shield-halved"></i> Dica de Biomecânica & Segurança:
          </div>
          <span id="modal-safety" class="text-[11px] leading-normal">Mantenha a postura alinhada e controle a descida.</span>
        </div>
      </div>

      <button onclick="closeExerciseModal()" class="w-full mt-4 bg-cyan-600 hover:bg-cyan-500 text-white font-bold py-2.5 rounded-xl transition shadow-lg shadow-cyan-600/20 active:scale-95">
        Concluir Leitura
      </button>
    </div>
  </div>

  <!-- Information Modal (Corrida & Basquete) -->
  <div id="info-modal" class="fixed inset-0 z-50 bg-black/85 backdrop-blur-md flex items-end sm:items-center justify-center p-0 sm:p-4 hidden">
    <div class="bg-slate-900 border border-slate-800 w-full max-w-md rounded-t-3xl sm:rounded-2xl p-5 max-h-[85vh] overflow-y-auto">
      <div class="flex justify-between items-start mb-3">
        <h3 id="info-modal-title" class="text-base font-bold text-white">Atividade Complementar</h3>
        <button onclick="closeInfoModal()" class="w-8 h-8 rounded-full bg-slate-800 text-slate-400 hover:text-white flex items-center justify-center transition">
          <i class="fa-solid fa-xmark"></i>
        </button>
      </div>
      <div id="info-modal-content" class="text-xs text-slate-300 space-y-3 leading-relaxed">
        <!-- Dynamic content -->
      </div>
      <button onclick="closeInfoModal()" class="w-full mt-4 bg-slate-800 hover:bg-slate-700 text-white font-bold py-2.5 rounded-xl transition">
        Fechar
      </button>
    </div>
  </div>

  <!-- Diagnostic Modal for testing .png path resolution on GitHub Pages -->
  <div id="diagnostic-modal" class="fixed inset-0 z-50 bg-black/90 backdrop-blur-md flex items-end sm:items-center justify-center p-0 sm:p-4 hidden">
    <div class="bg-slate-900 border border-slate-800 w-full max-w-lg rounded-t-3xl sm:rounded-2xl p-5 max-h-[85vh] overflow-y-auto custom-scroll">
      <div class="flex justify-between items-center mb-3">
        <div>
          <h3 class="text-base font-bold text-white flex items-center gap-2">
            <i class="fa-solid fa-network-wired text-cyan-400"></i> Diagnóstico da Pasta imagens/
          </h3>
          <p class="text-[11px] text-slate-400">Status em tempo real das imagens .PNG no seu GitHub Pages</p>
        </div>
        <button onclick="closeDiagnosticModal()" class="w-8 h-8 rounded-full bg-slate-800 text-slate-400 hover:text-white flex items-center justify-center transition">
          <i class="fa-solid fa-xmark"></i>
        </button>
      </div>

      <div class="space-y-2 mb-4 text-xs" id="diagnostic-results">
        <div class="p-3 rounded-xl bg-slate-950 text-slate-400 text-center">
          Clique no botão abaixo para testar as conexões HTTP das imagens.
        </div>
      </div>

      <div class="flex gap-2">
        <button onclick="runImageDiagnostics()" class="flex-1 bg-cyan-600 hover:bg-cyan-500 text-white font-bold py-2.5 rounded-xl text-xs transition active:scale-95 flex items-center justify-center gap-2">
          <i class="fa-solid fa-play"></i> Iniciar Verificação das Imagens
        </button>
        <button onclick="closeDiagnosticModal()" class="px-4 bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold py-2.5 rounded-xl text-xs transition">
          Fechar
        </button>
      </div>
    </div>
  </div>

  <nav class="fixed bottom-0 left-0 right-0 z-40 bg-[#0c121e]/95 backdrop-blur-lg border-t border-slate-800 py-2">
    <div class="max-w-lg mx-auto px-4 flex justify-around items-center">
      <button onclick="switchTab('workouts')" id="nav-workouts" class="flex flex-col items-center gap-1 active-nav-btn transition">
        <i class="fa-solid fa-dumbbell text-lg"></i>
        <span class="text-[10px]">Treinos</span>
      </button>
      <button onclick="switchTab('nutrition')" id="nav-nutrition" class="flex flex-col items-center gap-1 text-slate-400 hover:text-purple-400 transition">
        <i class="fa-solid fa-bowl-food text-lg"></i>
        <span class="text-[10px]">Nutrição</span>
      </button>
      <button onclick="switchTab('gallery')" id="nav-gallery" class="flex flex-col items-center gap-1 text-slate-400 hover:text-cyan-400 transition">
        <i class="fa-solid fa-images text-lg"></i>
        <span class="text-[10px]">Guia Visual</span>
      </button>
      <button onclick="switchTab('progress')" id="nav-progress" class="flex flex-col items-center gap-1 text-slate-400 hover:text-emerald-400 transition">
        <i class="fa-solid fa-chart-line text-lg"></i>
        <span class="text-[10px]">Progresso</span>
      </button>
    </div>
  </nav>

  <script>
    // Fallback SVG data generator so an image never looks broken
    function generateFallbackSVG(title, accent) {
      const bg = '#0f172a';
      const color = accent || '#38bdf8';
      const svg = `
        <svg xmlns="http://www.w3.org/2000/svg" width="600" height="400" viewBox="0 0 600 400" fill="none">
          <rect width="600" height="400" fill="${bg}"/>
          <circle cx="300" cy="170" r="50" fill="${color}" fill-opacity="0.15" stroke="${color}" stroke-width="2"/>
          <path d="M260 250 L340 250 M300 230 L300 270" stroke="${color}" stroke-width="3" stroke-linecap="round"/>
          <text x="300" y="320" text-anchor="middle" fill="#f8fafc" font-family="sans-serif" font-size="18" font-weight="bold">${title}</text>
          <text x="300" y="350" text-anchor="middle" fill="#94a3b8" font-family="sans-serif" font-size="12">Foto da pasta imagens/</text>
        </svg>
      `;
      return 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(svg);
    }

    // Helper to generate safe URL candidates (handles UTF-8 accents and space encoding)
    function buildImageCandidatePaths(baseList) {
      const extensions = ['.png', '.PNG', '.jpg', '.jpeg', '.webp'];
      const candidates = [];
      baseList.forEach(rawBase => {
        extensions.forEach(ext => {
          const direct = `${rawBase}${ext}`;
          const encoded = encodeURI(direct);
          if (!candidates.includes(direct)) candidates.push(direct);
          if (direct !== encoded && !candidates.includes(encoded)) candidates.push(encoded);
        });
      });
      return candidates;
    }

    // Direct database mapped with .png primary priority, URL variations and exact filenames
    const exercisesDB = {
      // PUSH - Exact requested filenames in PNG format
      supino_reto: {
        id: "supino_reto",
        name: "Supino Reto com Barra",
        category: "Peitoral Maior • Tríceps • Ombro",
        workout: "push",
        series: "4 séries",
        reps: "6 a 10 reps",
        rest: "90s - 120s",
        imgBaseNames: ["imagens/Supino", "imagens/supino"],
        img: "imagens/Supino.png",
        muscles: ["Peitoral Maior", "Tríceps Braquial", "Deltoide Anterior"],
        steps: [
          "Deite no banco com os olhos alinhados diretamente abaixo da barra.",
          "Retraia e deprima as escápulas contra o banco ('feche as asas').",
          "Desça a barra controlando o peso até encostar na linha média/inferior do peito.",
          "Empurre a barra de forma potente mantendo os pés cravados no chão."
        ],
        safety: "Mantenha os cotovelos a cerca de 60° em relação ao tronco para proteger o manguito rotador."
      },
      desenvolvimento_halteres: {
        id: "desenvolvimento_halteres",
        name: "Desenvolvimento com Halteres",
        category: "Deltoide Anterior & Lateral • Tríceps",
        workout: "push",
        series: "3 séries",
        reps: "8 a 12 reps",
        rest: "90s",
        imgBaseNames: [
          "imagens/Desenvolvimento com Halteres",
          "imagens/desenvolvimento com halteres",
          "imagens/desenvolvimento-com-halteres",
          "imagens/desenvolvimento"
        ],
        img: "imagens/Desenvolvimento com Halteres.png",
        muscles: ["Deltoide Anterior", "Deltoide Lateral", "Tríceps Braquial", "Trapézio"],
        steps: [
          "Sentado no banco com apoio nas costas, comece com os halteres na altura dos ombros.",
          "Cotovelos levemente à frente no plano escapular (~30° à frente da linha do corpo).",
          "Empurre os halteres para cima sem bater um no outro no topo.",
          "Desça de forma controlada até o nível do queixo."
        ],
        safety: "Mantenha o abdômen firme para não arquear a coluna lombar na subida."
      },
      crucifixo_halteres: {
        id: "crucifixo_halteres",
        name: "Crucifixo com Halteres",
        category: "Isolamento de Peitoral • Alongamento Máximo",
        workout: "push",
        series: "3 séries",
        reps: "10 a 12 reps",
        rest: "75s",
        imgBaseNames: ["imagens/Crucifixo", "imagens/crucifixo"],
        img: "imagens/Crucifixo.png",
        muscles: ["Peitoral Maior", "Deltoide Anterior", "Bíceps (Estabilizador)"],
        steps: [
          "Deitado no banco reto com um halter em cada mão apontando para cima.",
          "Mantenha uma leve flexão nos cotovelos durante todo o arco de descida.",
          "Abra os braços até sentir um alongamento profundo e confortável no peito.",
          "Feche os braços como se estivesse abraçando um barril grande."
        ],
        safety: "Não deixe os cotovelos descerem além do nível do banco se sentir desconforto nos ombros."
      },
      triceps_corda: {
        id: "triceps_corda",
        name: "Tríceps Corda no Pulley",
        category: "Tríceps Braquial (Cabeça Lateral e Longa)",
        workout: "push",
        series: "3 séries",
        reps: "10 a 15 reps",
        rest: "60s",
        imgBaseNames: [
          "imagens/Tríceps",
          "imagens/tríceps",
          "imagens/Triceps",
          "imagens/triceps"
        ],
        img: "imagens/Tríceps.png",
        muscles: ["Tríceps Braquial", "Ancôneo", "Extensores do Punho"],
        steps: [
          "Tronco levemente inclinado à frente com cotovelos colados ao lado da caixa torácica.",
          "Empurre a corda para baixo estendendo os braços.",
          "No ponto mais baixo, abra as pontas da corda para fora para contração máxima.",
          "Suba de volta controlando até o ângulo de 90° no cotovelo."
        ],
        safety: "Evite movimentar os ombros ou balançar o tronco para pegar impulso."
      },
      flexao_braco: {
        id: "flexao_braco",
        name: "Flexão de Braço",
        category: "Finalizador de Volume • Peitoral e Core",
        workout: "push",
        series: "3 séries",
        reps: "Até a falha técnica",
        rest: "60s",
        imgBaseNames: [
          "imagens/flexao",
          "imagens/Flexao",
          "imagens/flexão",
          "imagens/Flexão"
        ],
        img: "imagens/flexao.png",
        muscles: ["Peitoral Maior", "Core Abdominal", "Deltoide Anterior", "Tríceps"],
        steps: [
          "Posicione as mãos um pouco mais largas que a linha dos ombros.",
          "Mantenha o corpo como uma prancha rígida dos calcanhares à cabeça.",
          "Desça até o peito quase encostar no chão com cotovelos a ~45°.",
          "Empurre o solo de volta com firmeza."
        ],
        safety: "Não deixe o quadril cair nem arqueie a lombar durante as repetições finais."
      },

      // PULL
      puxada_pulley: {
        id: "puxada_pulley",
        name: "Puxada Frontal no Pulley (Lat Pulldown)",
        category: "Dorsais • Largura das Costas (V-Taper)",
        workout: "pull",
        series: "4 séries",
        reps: "6 a 10 reps",
        rest: "90s - 120s",
        imgBaseNames: ["imagens/Puxada", "imagens/puxada"],
        img: "imagens/Puxada.png",
        muscles: ["Latissimus Dorsi (Grande Dorsal)", "Redondo Maior", "Bíceps Braquial", "Romboides"],
        steps: [
          "Ajuste a almofada da coxa para fixar firmemente o corpo no banco.",
          "Segure a barra com pegada pronada na largura dos ombros ou ligeiramente maior.",
          "Inicie deprimindo as escápulas e puxe a barra na direção da clavícula.",
          "Retorne controlando o peso até os braços estenderem completamente no topo."
        ],
        safety: "Nunca puxe a barra por trás da cabeça para não forçar a coluna cervical."
      },
      remada_curvada: {
        id: "remada_curvada",
        name: "Remada Curvada com Barra (Bent-Over Row)",
        category: "Espessura de Costas • Trapézio & Romboides",
        workout: "pull",
        series: "4 séries",
        reps: "8 a 12 reps",
        rest: "90s",
        imgBaseNames: ["imagens/Remada Curvada", "imagens/remada-curvada", "imagens/remada_curvada", "imagens/remada"],
        img: "imagens/Remada Curvada.png",
        muscles: ["Trapézio Médio/Inferior", "Romboides", "Dorsais", "Deltoide Posterior", "Eretores"],
        steps: [
          "Com os joelhos destravados, incline o tronco mantendo as costas retas e o peito aberto.",
          "Segure a barra com pegada na largura dos ombros.",
          "Puxe a barra em direção ao umbigo conduzindo a força com os cotovelos para trás.",
          "Aperte as escápulas por 1 segundo no pico do movimento e desça controlando."
        ],
        safety: "Mantenha o core rígido. Se sentir a lombar, reduza o peso ou aumente o apoio."
      },
      remada_unilateral: {
        id: "remada_unilateral",
        name: "Remada Unilateral com Halter (Serrote)",
        category: "Densidade Dorsal Unilateral • Postura Correta",
        workout: "pull",
        series: "3 séries",
        reps: "10 a 12 reps cada lado",
        rest: "75s",
        imgBaseNames: ["imagens/Remada Unilateral", "imagens/serrote", "imagens/remada_unilateral"],
        img: "imagens/Remada Unilateral.png",
        muscles: ["Grande Dorsal", "Romboides", "Deltoide Posterior", "Bíceps"],
        steps: [
          "Apoie um joelho e a mão do mesmo lado sobre o banco reto.",
          "Mantenha a coluna neutra e o pescoço alinhado olhando para baixo.",
          "Puxe o halter na direção do quadril sem girar a coluna.",
          "Desça o halter alongando bem a dorsal sem deixar o ombro despencar."
        ],
        safety: "Evite balançar o corpo ou dar solavancos para subir o peso."
      },
      rosca_direta: {
        id: "rosca_direta",
        name: "Rosca Direta com Barra (Barbell Curl)",
        category: "Braços • Bíceps Braquial Completo",
        workout: "pull",
        series: "3 séries",
        reps: "8 a 12 reps",
        rest: "60s",
        imgBaseNames: ["imagens/Rosca Direta", "imagens/rosca-direta", "imagens/rosca_direta", "imagens/biceps"],
        img: "imagens/Rosca Direta.png",
        muscles: ["Bíceps Braquial (Cabeça Curta & Longa)", "Braquial Anterior", "Braquiorradial"],
        steps: [
          "Em pé com postura ereta e pés na largura dos ombros.",
          "Segure a barra com as palmas voltadas para a frente.",
          "Flexione os cotovelos elevando a barra até a contração máxima do bíceps.",
          "Desça em 2 a 3 segundos resistindo à gravidade até esticar quase por completo."
        ],
        safety: "Não balance as costas nem jogue o quadril para frente para compensar a carga."
      },

      // LEGS
      agachamento_livre: {
        id: "agachamento_livre",
        name: "Agachamento Livre com Barra (Back Squat)",
        category: "Pernas • Quadríceps, Glúteos & Core",
        workout: "legs",
        series: "4 séries",
        reps: "6 a 10 reps",
        rest: "120s",
        imgBaseNames: ["imagens/Agachamento", "imagens/agachamento"],
        img: "imagens/Agachamento.png",
        muscles: ["Quadríceps Femoral", "Glúteo Máximo", "Adutores", "Eretores da Espinha"],
        steps: [
          "Apoie a barra firme sobre a musculatura do trapézio e tire do suporte.",
          "Pés na largura dos ombros com pontas levemente voltadas para fora.",
          "Inicie flexionando os joelhos e o quadril como se fosse sentar num banco baixo.",
          "Desça até as coxas ficarem paralelas ao chão e suba empurrando o chão pelo calcanhar."
        ],
        safety: "Mantenha os joelhos apontando na mesma direção da ponta dos pés; nunca deixe entrarem para dentro."
      },
      terra_romeno: {
        id: "terra_romeno",
        name: "Levantamento Terra Romeno (RDL)",
        category: "Cadeia Posterior • Glúteos & Isquiotibiais",
        workout: "legs",
        series: "4 séries",
        reps: "8 a 12 reps",
        rest: "90s",
        imgBaseNames: ["imagens/Terra Romeno", "imagens/terra-romeno", "imagens/rdl"],
        img: "imagens/Terra Romeno.png",
        muscles: ["Isquiotibiais", "Glúteo Máximo", "Eretores da Coluna"],
        steps: [
          "Segure a barra com pegada pronada na largura das pernas.",
          "Mantenha os joelhos semi-flexionados fixos nessa posição.",
          "Empurre o quadril para trás mantendo a barra raspando rente às pernas.",
          "Ao sentir o alongamento máximo dos posteriores de coxa, estenda o quadril contraindo os glúteos."
        ],
        safety: "Mantenha as costas 100% retas durante todo o percurso; não arredonde a lombar."
      },
      leg_press: {
        id: "leg_press",
        name: "Leg Press 45°",
        category: "Quadríceps & Glúteos • Carga Segura",
        workout: "legs",
        series: "3 séries",
        reps: "10 a 12 reps",
        rest: "90s",
        imgBaseNames: ["imagens/Leg Press", "imagens/leg-press"],
        img: "imagens/Leg Press.png",
        muscles: ["Quadríceps", "Glúteo Máximo", "Panturrilhas"],
        steps: [
          "Acomode a lombar e os glúteos completamente colados no encosto.",
          "Posicione os pés na largura dos ombros no meio da plataforma.",
          "Destrave a máquina e desça a plataforma até formar 90° nos joelhos.",
          "Empurre de volta estendendo as pernas sem 'trancar' os joelhos no final."
        ],
        safety: "Nunca descole o bumbum do banco no final da descida para proteger os discos lombares."
      },
      cadeira_extensora: {
        id: "cadeira_extensora",
        name: "Cadeira Extensora (Leg Extension)",
        category: "Isolamento Completo de Quadríceps",
        workout: "legs",
        series: "3 séries",
        reps: "12 a 15 reps",
        rest: "60s",
        imgBaseNames: ["imagens/Cadeira Extensora", "imagens/extensora"],
        img: "imagens/Cadeira Extensora.png",
        muscles: ["Quadríceps Femoral"],
        steps: [
          "Ajuste o encosto de modo que o joelho fique no mesmo eixo de rotação da máquina.",
          "Apoie a almofada sobre a frente dos tornozelos.",
          "Estenda as pernas até a contração total e segure 1 segundo no topo.",
          "Desça suavemente controlando a descida do peso."
        ],
        safety: "Evite dar trancos explosivos com cargas acima do seu controle articular."
      },
      panturrilha_pe: {
        id: "panturrilha_pe",
        name: "Panturrilha em Pé com Halteres",
        category: "Panturrilha • Salto & Estabilidade de Basquete",
        workout: "legs",
        series: "4 séries",
        reps: "15 a 20 reps",
        rest: "60s",
        imgBaseNames: ["imagens/Panturrilha", "imagens/panturrilha"],
        img: "imagens/Panturrilha.png",
        muscles: ["Gastrocnêmio", "Sóleo", "Tibial Posterior"],
        steps: [
          "Apoie a ponta dos pés em um degrau ou step segurando um halter firme em cada mão.",
          "Desça os calcanhares para sentir o alongamento máximo da panturrilha.",
          "Suba na ponta dos pés com potência e congele 1 segundo no ponto mais alto.",
          "Desça de forma suave e pausada."
        ],
        safety: "Evite 'quicar' rápido; o controle da descida é o segredo para crescer panturrilha."
      },

      // FUNCTIONAL / EXTRA
      wall_sit: {
        id: "wall_sit",
        name: "Wall Sit (Agachamento Isométrico na Parede)",
        category: "Isometria • Fortalecimento do Joelho & Tendão Patelar",
        workout: "legs",
        series: "3 séries",
        reps: "35 a 45 segundos",
        rest: "60s",
        imgBaseNames: ["imagens/Wall Sit", "imagens/wall-sit"],
        img: "imagens/Wall Sit.png",
        muscles: ["Quadríceps", "Estabilizadores do Joelho", "Glúteos"],
        steps: [
          "Apoie as costas retas na parede e deslize até os joelhos ficarem em ângulo de 90°.",
          "Pés firmes no chão na largura dos ombros.",
          "Não apoie as mãos nas coxas.",
          "Respire ritmicamente sustentando a contração isométrica."
        ],
        safety: "Essencial para proteger os tendões se você joga basquete ou corre com frequência."
      },
      step_up: {
        id: "step_up",
        name: "Step-Up na Caixa ou Banco",
        category: "Unilateral • Pliometria, Salto Vertical & Glúteos",
        workout: "legs",
        series: "3 séries",
        reps: "10 a 12 reps cada perna",
        rest: "75s",
        imgBaseNames: ["imagens/Step Up", "imagens/step-up"],
        img: "imagens/Step Up.png",
        muscles: ["Glúteo Máximo", "Quadríceps", "Panturrilhas"],
        steps: [
          "Pise com todo o pé sobre a caixa ou banco estável.",
          "Empurre pelo calcanhar da perna que está em cima para elevar o corpo.",
          "Fique completamente ereto no topo antes de descer de volta com controle."
        ],
        safety: "Não pegue impulso com a perna de trás no chão; deixe a perna de cima fazer a força."
      }
    };

    // Sequential multi-extension fallback handler focusing on .png and URL-encoding
    function handleImageError(imgElement) {
      const exerciseId = imgElement.getAttribute('data-ex-id');
      const ex = exercisesDB[exerciseId];
      if (!ex) return;

      const candidates = buildImageCandidatePaths(ex.imgBaseNames || [`imagens/${ex.name}`]);
      let attempt = parseInt(imgElement.getAttribute('data-attempt') || '0', 10);

      if (attempt < candidates.length) {
        imgElement.setAttribute('data-attempt', (attempt + 1).toString());
        imgElement.src = candidates[attempt];
      } else {
        // Stop retrying and show clear SVG fallback
        imgElement.onerror = null;
        imgElement.src = generateFallbackSVG(ex.name, '#38bdf8');
      }
    }

    // Diagnostic Modal Logic
    function openDiagnosticModal() {
      document.getElementById('diagnostic-modal').classList.remove('hidden');
      runImageDiagnostics();
    }

    function closeDiagnosticModal() {
      document.getElementById('diagnostic-modal').classList.add('hidden');
    }

    async function checkUrl(url) {
      try {
        const response = await fetch(url, { method: 'HEAD' });
        return { ok: response.ok, status: response.status };
      } catch (err) {
        return { ok: false, status: 'Erro de Rede / CORS' };
      }
    }

    async function runImageDiagnostics() {
      const container = document.getElementById('diagnostic-results');
      container.innerHTML = `
        <div class="p-3 bg-slate-950 rounded-xl text-center text-cyan-400 font-bold text-xs flex items-center justify-center gap-2">
          <i class="fa-solid fa-spinner fa-spin"></i> Testando arquivos .png na pasta imagens/...
        </div>
      `;

      const pushKeys = workoutRoutines.push;
      let html = '<div class="space-y-2">';

      for (const key of pushKeys) {
        const ex = exercisesDB[key];
        const candidates = buildImageCandidatePaths(ex.imgBaseNames).slice(0, 3);
        let foundCandidate = null;

        for (const path of candidates) {
          const res = await checkUrl(path);
          if (res.ok) {
            foundCandidate = { path, status: res.status };
            break;
          }
        }

        if (foundCandidate) {
          html += `
            <div class="p-2.5 bg-emerald-950/30 border border-emerald-500/40 rounded-xl flex items-center justify-between text-xs">
              <div>
                <span class="font-bold text-white block">${ex.name}</span>
                <span class="text-[10px] text-emerald-400 font-mono">${foundCandidate.path}</span>
              </div>
              <span class="px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 font-bold text-[10px]">200 OK</span>
            </div>
          `;
        } else {
          const defaultPath = `${ex.imgBaseNames[0]}.png`;
          html += `
            <div class="p-2.5 bg-rose-950/30 border border-rose-500/40 rounded-xl flex flex-col gap-1 text-xs">
              <div class="flex items-center justify-between">
                <span class="font-bold text-white">${ex.name}</span>
                <span class="px-2 py-0.5 rounded bg-rose-500/20 text-rose-300 font-bold text-[10px]">404 Não Encontrado</span>
              </div>
              <div class="text-[10px] text-slate-400 font-mono truncate">Testado: ${defaultPath}</div>
              <div class="text-[10px] text-amber-300">Verifique se o arquivo está exatamente em <code class="bg-slate-900 px-1 rounded">${defaultPath}</code> no GitHub.</div>
            </div>
          `;
        }
      }

      html += '</div>';
      container.innerHTML = html;
    }

    function openExerciseModal(id) {
      const ex = exercisesDB[id];
      if (!ex) return;

      currentModalExerciseId = id;
      document.getElementById('modal-category').innerText = `Treino ${ex.workout.toUpperCase()} • ${ex.category}`;
      document.getElementById('modal-title').innerText = ex.name;
      document.getElementById('modal-safety').innerText = ex.safety;

      const imgEl = document.getElementById('modal-image');
      imgEl.setAttribute('data-ex-id', id);
      imgEl.setAttribute('data-attempt', '0');
      imgEl.src = getExerciseImage(id);

      // Render muscles badges
      const musclesContainer = document.getElementById('modal-muscles');
      musclesContainer.innerHTML = ex.muscles.map(m => `
        <span class="bg-slate-800 text-cyan-300 px-2.5 py-0.5 rounded-full text-[11px] font-semibold border border-slate-700">
          ${m}
        </span>
      `).join('');

      // Render steps
      const stepsContainer = document.getElementById('modal-steps');
      stepsContainer.innerHTML = ex.steps.map(s => `<li>${s}</li>`).join('');

      document.getElementById('exercise-modal').classList.remove('hidden');
    }

    function closeExerciseModal() {
      document.getElementById('exercise-modal').classList.add('hidden');
      currentModalExerciseId = null;
    }

    // Handle Custom User Photo Upload
    function handleUserPhotoUpload(event) {
      const file = event.target.files[0];
      if (!file || !currentModalExerciseId) return;

      const reader = new FileReader();
      reader.onload = function(e) {
        const base64Img = e.target.result;
        try {
          localStorage.setItem(`custom_img_${currentModalExerciseId}`, base64Img);
          document.getElementById('modal-image').src = base64Img;
          renderWorkoutExercises();
          renderGallery('all');
        } catch (err) {
          console.warn("Storage quota limit reached for local images", err);
        }
      };
      reader.readAsDataURL(file);
    }

    function renderGallery(filter) {
      const grid = document.getElementById('gallery-grid');
      let keys = Object.keys(exercisesDB);

      if (filter !== 'all') {
        keys = keys.filter(k => exercisesDB[k].workout === filter);
      }

      let html = '';
      keys.forEach(key => {
        const ex = exercisesDB[key];
        const imgSrc = getExerciseImage(key);

        html += `
          <div onclick="openExerciseModal('${key}')" class="bg-slate-950 border border-slate-800 rounded-xl overflow-hidden cursor-pointer hover:border-cyan-500 transition group p-2">
            <div class="w-full h-28 bg-slate-900 rounded-lg overflow-hidden relative mb-2 flex items-center justify-center">
              <img src="${imgSrc}" alt="${ex.name}" data-ex-id="${key}" data-attempt="0" class="w-full h-full object-contain group-hover:scale-105 transition duration-300" onerror="handleImageError(this)">
              <span class="absolute top-1.5 left-1.5 bg-black/70 text-[9px] font-bold text-white px-1.5 py-0.5 rounded border border-white/10 uppercase">
                ${ex.workout}
              </span>
            </div>
            <h5 class="text-xs font-bold text-white truncate leading-tight group-hover:text-cyan-400">${ex.name}</h5>
            <div class="text-[10px] text-slate-400 mt-0.5 truncate">${ex.category.split('•')[0]}</div>
          </div>
        `;
      });

      grid.innerHTML = html;
    }

    function filterGallery(filter) {
      document.querySelectorAll('.gallery-filter-btn').forEach(btn => {
        btn.className = "gallery-filter-btn px-3 py-1 rounded-lg text-xs font-semibold bg-slate-800 text-slate-300 hover:bg-slate-700 flex-shrink-0";
      });
      event.target.className = "gallery-filter-btn px-3 py-1 rounded-lg text-xs font-bold bg-cyan-600 text-white flex-shrink-0";
      renderGallery(filter);
    }

    function saveExerciseLog(id, field, value) {
      localStorage.setItem(`${field}_${id}`, value);
    }

    function toggleExerciseDone(id) {
      const current = localStorage.getItem(`done_${id}`) === 'true';
      const next = !current;
      localStorage.setItem(`done_${id}`, next);

      if (next) {
        startRest(90);
      }
      renderWorkoutExercises();
    }

    // Beep sound with Web Audio API
    function playBeep() {
      try {
        const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(800, audioCtx.currentTime);
        gain.gain.setValueAtTime(0.1, audioCtx.currentTime);
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start();
        osc.stop(audioCtx.currentTime + 0.25);
      } catch (e) {
        // AudioContext not permitted or blocked
      }
    }

    function startRest(seconds) {
      clearInterval(timerInterval);
      timerSeconds = seconds;
      updateTimerUI();

      timerInterval = setInterval(() => {
        timerSeconds--;
        updateTimerUI();
        if (timerSeconds <= 0) {
          clearInterval(timerInterval);
          playBeep();
          if (navigator.vibrate) navigator.vibrate([200, 100, 200]);
        }
      }, 1000);
    }

    function stopRest() {
      clearInterval(timerInterval);
      timerSeconds = 0;
      updateTimerUI();
    }

    function updateTimerUI() {
      const mins = Math.floor(timerSeconds / 60);
      const secs = timerSeconds % 60;
      document.getElementById('timer-text').innerText = 
        `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
    }

    function addWater(amount) {
      waterCurrent = Math.min(waterGoal, waterCurrent + amount);
      updateWaterUI();
      localStorage.setItem('water_ml', waterCurrent);
    }

    function resetWater() {
      waterCurrent = 0;
      updateWaterUI();
      localStorage.setItem('water_ml', waterCurrent);
    }

    function updateWaterUI() {
      document.getElementById('water-text').innerText = `${waterCurrent} / ${waterGoal} ml`;
      const pct = Math.min(100, (waterCurrent / waterGoal) * 100);
      document.getElementById('water-bar').style.width = `${pct}%`;
    }

    function loadSavedWater() {
      const saved = localStorage.getItem('water_ml');
      if (saved) {
        waterCurrent = parseInt(saved, 10);
        updateWaterUI();
      }
    }

    function toggleMealCheck(idx, checked) {
      localStorage.setItem(`meal_chk_${idx}`, checked ? 'true' : 'false');
    }

    function loadSavedMeals() {
      for (let i = 1; i <= 5; i++) {
        const isChecked = localStorage.getItem(`meal_chk_${i}`) === 'true';
        const el = document.getElementById(`chk-meal-${i}`);
        if (el) el.checked = isChecked;
      }
    }

    function loadWeightHistory() {
      const history = JSON.parse(localStorage.getItem('weight_history') || '[]');
      const list = document.getElementById('weight-history-list');

      if (history.length === 0) {
        list.innerHTML = `
          <li class="flex justify-between pt-1">
            <span class="text-slate-400">Semana 1 (Início)</span>
            <span class="font-bold text-white">78.0 kg</span>
          </li>
          <li class="flex justify-between pt-1">
            <span class="text-slate-400">Semana 2</span>
            <span class="font-bold text-emerald-400">78.4 kg (+400g)</span>
          </li>
        `;
        return;
      }

      list.innerHTML = history.map(item => `
        <li class="flex justify-between pt-1">
          <span class="text-slate-400">${item.date}</span>
          <span class="font-bold text-emerald-400">${item.weight} kg</span>
        </li>
      `).join('');
    }

    function promptNewWeight() {
      const weightVal = prompt("Digite seu peso em jejum hoje (ex: 78.8):");
      if (weightVal && !isNaN(parseFloat(weightVal))) {
        const history = JSON.parse(localStorage.getItem('weight_history') || '[]');
        const today = new Date().toLocaleDateString('pt-BR', { day: '2-digit', month: '2-digit' });
        history.unshift({
          date: `Pesagem (${today})`,
          weight: parseFloat(weightVal).toFixed(1)
        });
        localStorage.setItem('weight_history', JSON.stringify(history));
        loadWeightHistory();
      }
    }

    // Complementary Activities Modal
    function openInfoModal(type) {
      const modal = document.getElementById('info-modal');
      const title = document.getElementById('info-modal-title');
      const content = document.getElementById('info-modal-content');

      if (type === 'corrida') {
        title.innerHTML = `<i class="fa-solid fa-person-running text-amber-400 mr-2"></i> Corrida Leve (Zona 2)`;
        content.innerHTML = `
          <div class="bg-slate-800/60 p-3 rounded-xl border border-slate-700/50">
            <strong class="text-white block mb-1">Como correr sem perder massa muscular:</strong>
            <p>Faça de 20 a 30 minutos em ritmo conversacional (Zona 2: onde você consegue falar sem perder o fôlego).</p>
          </div>
          <ul class="list-disc list-inside space-y-1.5 text-slate-300">
            <li><strong>Melhor dia:</strong> Em dias sem musculação ou com pelo menos 6h de distância do treino de pernas.</li>
            <li><strong>Benefício:</strong> Aumenta a capilarização periférica e acelera o transporte de nutrientes aos músculos.</li>
            <li><strong>Dica:</strong> Beba água antes e tome um shake com carboidrato ao terminar.</li>
          </ul>
        `;
      } else {
        title.innerHTML = `<i class="fa-solid fa-basketball text-orange-400 mr-2"></i> Basquete & Gestão de Pernas`;
        content.innerHTML = `
          <div class="bg-slate-800/60 p-3 rounded-xl border border-slate-700/50">
            <strong class="text-white block mb-1">Impacto articular e saltos:</strong>
            <p>O basquete exige sprints e saltos que demandam muito dos quadríceps, tendões e panturrilha.</p>
          </div>
          <ul class="list-disc list-inside space-y-1.5 text-slate-300">
            <li><strong>Regra de Ouro:</strong> Se jogou basquete forte (1h+), descanse as pernas e pule o <em>Treino C</em> dessa semana ou reduza o volume.</li>
            <li><strong>Combustível:</strong> Acrescente 40g a 50g extras de carboidrato para recuperar o glicogênio gasto nas corridas.</li>
            <li><strong>Proteção:</strong> Faça o exercício <em>Wall Sit</em> (agachamento isométrico na parede) no dia seguinte para desinflamar o tendão patelar.</li>
          </ul>
        `;
      }

      modal.classList.remove('hidden');
    }

    function closeInfoModal() {
      document.getElementById('info-modal').classList.add('hidden');
    }
  </script>
</body>
</html>
