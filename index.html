<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Application Showcase Hub</title>
    <!-- Tailwind CSS for sleek utility styling -->
    <script src="https://tailwindcss.com"></script>
</head>
<body class="bg-slate-900 text-slate-100 min-h-screen flex flex-col font-sans">

    <!-- Header Navigation -->
    <header class="border-b border-slate-800 bg-slate-900/50 backdrop-blur sticky top-0 z-50">
        <div class="max-w-6xl mx-auto px-4 h-16 flex items-center justify-between">
            <div class="flex items-center space-x-3">
                <div class="w-8 h-8 bg-indigo-500 rounded-lg flex items-center justify-center font-bold text-white">S</div>
                <span class="font-semibold text-lg tracking-tight">ShowcaseHub</span>
            </div>
            <nav class="flex space-x-6 text-sm font-medium text-slate-400">
                <a href="#" class="hover:text-indigo-400 transition">Overview</a>
                <a href="https://github.com" target="_blank" class="hover:text-indigo-400 transition">Repository</a>
            </nav>
        </div>
    </header>

    <!-- Main Content Area -->
    <main class="flex-grow max-w-6xl w-full mx-auto px-4 py-12">
        
        <!-- Hero Title Banner -->
        <section class="text-center max-w-2xl mx-auto mb-16">
            <h1 class="text-4xl sm:text-5xl font-extrabold text-white tracking-tight mb-4">
                Full-Stack Application <span class="text-transparent bg-clip-text bg-gradient-to-r from-indigo-400 to-cyan-400">Showcase</span>
            </h1>
            <p class="text-lg text-slate-400">
                A streamlined proof-of-concept boilerplate connecting a Python Flask REST API backend with a dynamic Tailwind CSS frontend web interface.
            </p>
        </section>

        <!-- Dynamic Live App Metrics -->
        <section class="grid grid-cols-1 sm:grid-cols-3 gap-6 mb-16">
            <div class="bg-slate-800/50 border border-slate-800 rounded-xl p-6">
                <p class="text-xs font-semibold text-slate-500 uppercase tracking-wider mb-1">System Status</p>
                <p id="stat-uptime" class="text-2xl font-bold text-emerald-400">Loading...</p>
            </div>
            <div class="bg-slate-800/50 border border-slate-800 rounded-xl p-6">
                <p class="text-xs font-semibold text-slate-500 uppercase tracking-wider mb-1">Simulated Live Users</p>
                <p id="stat-users" class="text-2xl font-bold text-white">Loading...</p>
            </div>
            <div class="bg-slate-800/50 border border-slate-800 rounded-xl p-6">
                <p class="text-xs font-semibold text-slate-500 uppercase tracking-wider mb-1">API Throughput (24h)</p>
                <p id="stat-requests" class="text-2xl font-bold text-indigo-400">Loading...</p>
            </div>
        </section>

        <!-- Project Cards Title -->
        <section class="mb-8 flex items-center justify-between">
            <h2 class="text-2xl font-bold text-white tracking-tight">Featured Portfolio Projects</h2>
            <span class="px-2.5 py-1 text-xs font-semibold bg-indigo-500/10 text-indigo-400 rounded-full border border-indigo-500/20">API Sourced</span>
        </section>

        <!-- Async Project Dynamic Grid container -->
        <section id="projects-grid" class="grid grid-cols-1 md:grid-cols-3 gap-6">
            <!-- Skeleton items fallback before JS loads -->
            <div class="animate-pulse bg-slate-800 h-48 rounded-xl border border-slate-700"></div>
            <div class="animate-pulse bg-slate-800 h-48 rounded-xl border border-slate-700"></div>
            <div class="animate-pulse bg-slate-800 h-48 rounded-xl border border-slate-700"></div>
        </section>

    </main>

    <!-- Footer -->
    <footer class="border-t border-slate-800 bg-slate-950 py-6 text-center text-sm text-slate-500">
        <p>&copy; 2026 Repository Showcase. Open source template layout.</p>
    </footer>

    <!-- Frontend Functional Controller Logic -->
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            // Fetch system metrics from Flask API
            fetch('/api/stats')
                .then(res => res.json())
                .then(json => {
                    if(json.status === 'success') {
                        document.getElementById('stat-uptime').innerText = json.metrics.uptime;
                        document.getElementById('stat-users').innerText = json.metrics.active_users.toLocaleString();
                        document.getElementById('stat-requests').innerText = json.metrics.api_requests_24h.toLocaleString();
                    }
                })
                .catch(() => {
                    // Local fallback visualization if app runs without server layer directly
                    document.getElementById('stat-uptime').innerText = "Offline (Static Mode)";
                    document.getElementById('stat-users').innerText = "0";
                    document.getElementById('stat-requests').innerText = "0";
                });

            // Fetch structural items card layout list
            const grid = document.getElementById('projects-grid');
            fetch('/api/projects')
                .then(res => res.json())
                .then(json => {
                    if(json.status === 'success') {
                        grid.innerHTML = ''; // Wipe formatting placeholders out
                        json.data.forEach(project => {
                            const tags = project.tech_stack.map(tech => 
                                `<span class="text-xs bg-slate-800 text-slate-300 px-2 py-0.5 rounded border border-slate-700">${tech}</span>`
                            ).join(' ');

                            const card = `
                                <div class="bg-slate-900 border border-slate-800 rounded-xl p-6 hover:border-slate-700 hover:shadow-xl transition flex flex-col justify-between group">
                                    <div>
                                        <h3 class="text-lg font-bold text-white group-hover:text-indigo-400 transition mb-2">${project.title}</h3>
                                        <p class="text-sm text-slate-400 leading-relaxed mb-4">${project.description}</p>
                                    </div>
                                    <div class="flex flex-wrap gap-1.5 mt-auto pt-4 border-t border-slate-800/60">
                                        ${tags}
                                    </div>
                                </div>
                            `;
                            grid.innerHTML += card;
                        });
                    }
                })
                .catch(err => {
                    grid.innerHTML = `
                        <div class="col-span-full text-center py-8 text-amber-400 text-sm">
                            Unable to fetch dynamic server data. Please ensure <code class="bg-slate-800 px-1 py-0.5 rounded text-white text-xs">python app.py</code> is up and running.
                        </div>`;
                });
        });
    </script>
</body>
</html>
