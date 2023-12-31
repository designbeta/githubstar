class TopicsInfo(object):
    hotTopicsSet = {'3d',
                    '3ds-homebrew',
                    '4d-component',
                    '4x',
                    'abap',
                    'abapgit',
                    'action-adventure',
                    'action-game',
                    'action-role-playing',
                    'actions',
                    'actionscript',
                    'activitypub',
                    'ada',
                    'adobe-acrobat',
                    'advent-of-code',
                    'adventure-game',
                    'ai',
                    'ajax',
                    'algolia',
                    'algorithm',
                    'alloy-analyzer',
                    'alternate-reality-game',
                    'altium-designer',
                    'altv',
                    'amphp',
                    'android',
                    'android-library',
                    'android-studio',
                    'angular',
                    'angular-cli',
                    'anidb',
                    'animal-crossing',
                    'animation',
                    'anime',
                    'anki',
                    'ansible',
                    'ansible-role',
                    'antlr',
                    'api',
                    'apm',
                    'app',
                    'apple',
                    'apple-music',
                    'appwrite',
                    'arcade',
                    'archlinux',
                    'arduino',
                    'argo-floats',
                    'art-net',
                    'artillery-game',
                    'asgi',
                    'aspnet',
                    'assembly',
                    'assemblyscript',
                    'astro',
                    'astronomy',
                    'astrophysics',
                    'atom',
                    'aurelia',
                    'auth0',
                    'authentication',
                    'automation',
                    'avalonia',
                    'awesome',
                    'awesomewm',
                    'aws',
                    'azd-templates',
                    'azure',
                    'azure-devops',
                    'b4x',
                    'babel',
                    'backbonejs',
                    'backend',
                    'bash',
                    'basic8',
                    'batch-file',
                    'battle-royale',
                    'battlesnake',
                    'bcsamples',
                    'beat-em-up',
                    'bedrock-dedicated-server',
                    'bevy',
                    'bigquery',
                    'binance',
                    'bioinformatics',
                    'biological-expression-language',
                    'biological-simulation',
                    'bitcoin',
                    'bitcoin-cash',
                    'blazor',
                    'blockchain',
                    'blockly',
                    'blogger',
                    'board-game',
                    'boilerplate',
                    'boinc',
                    'bootstrap',
                    'bosque',
                    'bot',
                    'bridgetown',
                    'browser-game',
                    'bugbounty',
                    'bukkit',
                    'bulma',
                    'c',
                    'cadquery',
                    'calculate-pi',
                    'canvas',
                    'capnproto',
                    'cargo-generate',
                    'cassandra',
                    'casual-game',
                    'cdnjs',
                    'chaos-engineering',
                    'chatbot',
                    'chatgpt',
                    'chatgpt-api',
                    'christianity',
                    'chrome',
                    'chrome-extension',
                    'chromium',
                    'circuitpython',
                    'citizen-science',
                    'city-building-game',
                    'clash',
                    'classless',
                    'cli',
                    'client',
                    'climate-change',
                    'climate-change-mitigation',
                    'clojure',
                    'clojurescript',
                    'cloud-run',
                    'cloudflare',
                    'cms',
                    'coap',
                    'code-quality',
                    'code-review',
                    'codeception',
                    'codechef',
                    'collectible-card-game',
                    'combat-flight-simulator',
                    'common-lisp',
                    'compiler',
                    'composer',
                    'computer-algebra',
                    'computer-science',
                    'computer-vision',
                    'computercraft',
                    'computercraft-tweaked',
                    'conan',
                    'concourse-ci',
                    'configuration',
                    'contentful',
                    'continuous-integration',
                    'coq',
                    'cordova',
                    'coregames',
                    'coursera',
                    'covid-19',
                    'cpp',
                    'crawler',
                    'creative-commons',
                    'credo',
                    'cryptocurrency',
                    'cryptography',
                    'crystal',
                    'csg',
                    'csharp',
                    'css',
                    'css-modules',
                    'css-reset',
                    'cst',
                    'csv',
                    'cuda',
                    'curl',
                    'cve',
                    'cwl',
                    'd',
                    'dark-mode',
                    'dart',
                    'data',
                    'data-analysis',
                    'data-science',
                    'data-structures',
                    'data-visualization',
                    'database',
                    'dataops',
                    'debian',
                    'deep-learning',
                    'deep-neural-networks',
                    'demoscene',
                    'deno',
                    'dependency-management',
                    'deployer',
                    'deployment',
                    'deta',
                    'deta-space',
                    'developer-experience',
                    'devops',
                    'discord',
                    'discord-bots',
                    'discord-js',
                    'disk-image',
                    'django',
                    'dle',
                    'dll-injector',
                    'dmx512',
                    'docker',
                    'docker-compose',
                    'docker-image',
                    'dockerfile',
                    'documentation',
                    'dotfiles',
                    'dotnet',
                    'drupal',
                    'duckduckgo',
                    'dungeon-crawl',
                    'dwd',
                    'ebpf',
                    'ecmascript',
                    'edge',
                    'edi',
                    'education',
                    'edupage',
                    'effector',
                    'ejs',
                    'elasticsearch',
                    'electron',
                    'eleventy',
                    'elite-dangerous',
                    'elixir',
                    'elm',
                    'emacs',
                    'ember',
                    'emoji',
                    'emqx',
                    'emulator',
                    'end-to-end-encryption',
                    'ens',
                    'ensisa',
                    'entity-resolution',
                    'epics',
                    'epitech',
                    'erlang',
                    'error-propagation',
                    'escape-the-room',
                    'eslint',
                    'esolang',
                    'esp32',
                    'esp8266',
                    'esprit',
                    'ethereum',
                    'express',
                    'f-droid',
                    'fable',
                    'fabricmc',
                    'facebook',
                    'fantasy-console',
                    'fantasy-game',
                    'fastapi',
                    'fastify',
                    'feathers',
                    'fediverse',
                    'fedora',
                    'felgo',
                    'fighting-game',
                    'figma',
                    'finite-element-method',
                    'firebase',
                    'firefox',
                    'firefox-extension',
                    'first',
                    'first-person-shooter',
                    'first-robotics-competition',
                    'first-tech-challenge',
                    'fish',
                    'flask',
                    'flathub',
                    'flatpak',
                    'flight',
                    'flight-simulator',
                    'flightgear',
                    'flipperzero',
                    'flow-blockchain',
                    'fluent-design',
                    'flutter',
                    'font',
                    'fortran',
                    'frame-interpolation',
                    'framer-motion',
                    'framework',
                    'freeswitch',
                    'frontend',
                    'fsharp',
                    'functional-programming',
                    'game-development',
                    'game-engine',
                    'game-jam',
                    'game-jam-game',
                    'game-off',
                    'gameboy',
                    'gamemaker',
                    'garrysmod',
                    'gatsby',
                    'geneontology',
                    'generative-adversarial-network',
                    'genshin-impact',
                    'geode-mods',
                    'geometry-dash',
                    'getting-things-done',
                    'gh-extension',
                    'ghidra',
                    'gin',
                    'gis',
                    'giscus',
                    'git',
                    'gitea',
                    'github',
                    'github-api',
                    'github-desktop',
                    'gitlab',
                    'gitpod',
                    'glam',
                    'global-game-jam',
                    'gmail',
                    'go',
                    'god-game',
                    'godot',
                    'gogs',
                    'golem',
                    'golfing-language',
                    'google',
                    'google-admin',
                    'google-apps-script',
                    'google-calendar',
                    'google-chat',
                    'google-classroom',
                    'google-cloud',
                    'google-cloud-identity',
                    'google-docs',
                    'google-drive',
                    'google-forms',
                    'google-groups',
                    'google-keep',
                    'google-maps',
                    'google-meet',
                    'google-sheets',
                    'google-slides',
                    'google-tasks',
                    'google-vault',
                    'google-workspace',
                    'gpl',
                    'gradescope',
                    'gradle',
                    'grafana',
                    'graphql',
                    'grid-computing',
                    'groovy',
                    'grpc',
                    'gtfs',
                    'gui',
                    'guilded',
                    'guildwars2',
                    'gulp',
                    'guzzle',
                    'hack-and-slash',
                    'hackathon',
                    'hackathon-kit',
                    'hackathon-organiser',
                    'hackclub',
                    'hackerrank',
                    'hacktoberfest',
                    'handshake',
                    'haskell',
                    'haxe',
                    'heroku',
                    'highlightjs',
                    'hms',
                    'home-assistant',
                    'homebrew',
                    'homebridge',
                    'html',
                    'http',
                    'hugo',
                    'icon-font',
                    'identicons',
                    'ietf',
                    'image-processing',
                    'imagej',
                    'incremental-game',
                    'indieweb',
                    'inkscape',
                    'instagram',
                    'intellij-idea',
                    'interactive-fiction',
                    'interactive-film',
                    'ionic',
                    'ios',
                    'iot',
                    'ipfs',
                    'ipython',
                    'iris',
                    'iso-8601',
                    'itmo',
                    'jakarta-ee',
                    'jamstack',
                    'java',
                    'javafx',
                    'javascript',
                    'jekyll',
                    'jenkins',
                    'jest',
                    'jetbrains-mps',
                    'jetpack-compose',
                    'jquery',
                    'js13kgames',
                    'json',
                    'julia',
                    'jupyter-notebook',
                    'jwt',
                    'kakoune',
                    'kart-racing',
                    'keras',
                    'kerbal-space-program',
                    'kernel',
                    'kivy',
                    'koa',
                    'koans',
                    'kontent-ai',
                    'kotlin',
                    'kotlin-multiplatform',
                    'kubernetes',
                    'lamp',
                    'laravel',
                    'latex',
                    'league-of-legends',
                    'lean',
                    'less',
                    'libcloud',
                    'library',
                    'life-simulator',
                    'light-gun-shooter',
                    'liko-12',
                    'lineageos',
                    'linkstack',
                    'linux',
                    'lisp',
                    'll-parser',
                    'llvm',
                    'localization',
                    'low-code',
                    'lr-parser',
                    'lua',
                    'ludum-dare',
                    'luvit',
                    'm3o',
                    'machine-learning',
                    'macos',
                    'mada',
                    'mahapps',
                    'mainframe',
                    'markdown',
                    'massively-multiplayer-online',
                    'mastodon',
                    'material-design',
                    'material-design-for-bootstrap',
                    'mathcomp',
                    'mathematics',
                    'matlab',
                    'matrix-org',
                    'matter',
                    'maven',
                    'maze',
                    'mcfunction',
                    'mdx',
                    'mediawiki',
                    'medical-imaging',
                    'medium',
                    'megengine',
                    'meilisearch',
                    'mercury-lang',
                    'metroidvania',
                    'microformats',
                    'micropython',
                    'microservice',
                    'microsoft',
                    'midi',
                    'midi2',
                    'mikrotik',
                    'mill-plugin',
                    'minecraft',
                    'minecraft-addon',
                    'minecraft-bedrock-edition',
                    'minecraft-forge',
                    'minecraft-mod',
                    'minecraft-plugin',
                    'minecraft-server',
                    'minetest',
                    'mkdocs',
                    'mobile',
                    'molecular-dynamics',
                    'molecule',
                    'moleculer',
                    'monero',
                    'mongodb',
                    'mongoose',
                    'monitoring',
                    'motorola-68000',
                    'mount-and-blade-bannerlord',
                    'mozilla',
                    'mqtt',
                    'mud-game',
                    'music-game',
                    'musicxml',
                    'mvc',
                    'mvvmcross',
                    'myanimelist',
                    'mysql',
                    'nanocurrency',
                    'nasa',
                    'nashville',
                    'nativescript',
                    'nebula-graph',
                    'neo',
                    'neo4j',
                    'neovim',
                    'nestjs',
                    'netbox',
                    'netbox-plugin',
                    'netflix',
                    'netfree',
                    'netlify',
                    'nette',
                    'netty',
                    'neural-network',
                    'nextcloud',
                    'nextjs',
                    'nextra',
                    'nexus-mods',
                    'nginx',
                    'nhost',
                    'nim',
                    'nix',
                    'nlp',
                    'no-code',
                    'nodejs',
                    'nosql',
                    'npm',
                    'nuget',
                    'numpy',
                    'nunjucks',
                    'nuxt',
                    'nvidia',
                    'oai-pmh',
                    'objective-c',
                    'obofoundry',
                    'obsidian-md',
                    'ocaml',
                    'oculus',
                    'online-judge',
                    'open-access',
                    'open-data',
                    'open-graph',
                    'open-policy-agent',
                    'open-source',
                    'openacc',
                    'openbsd',
                    'opencomputers',
                    'opencv',
                    'openfaas',
                    'openfin',
                    'opengl',
                    'openstreetmap',
                    'opentelemetry',
                    'openui5',
                    'openutau',
                    'operating-system',
                    'oracle-database',
                    'orgmode',
                    'osint',
                    'p2p',
                    'package-manager',
                    'parsing',
                    'passkeys',
                    'password-store',
                    'perceptual-hashing',
                    'perl',
                    'pharo',
                    'phaser',
                    'photogrammetry',
                    'php',
                    'php-fusion',
                    'phpunit',
                    'physics',
                    'pico-8',
                    'pihole',
                    'pim',
                    'pip',
                    'pipewire',
                    'pixel-art',
                    'pixel-vision-8',
                    'pixiv',
                    'plaintext-accounting',
                    'platform-game',
                    'platformio',
                    'playwright',
                    'plover',
                    'pmmp',
                    'point-and-click',
                    'point-cloud',
                    'ponylang',
                    'portapps',
                    'portfolio',
                    'portugol',
                    'postgresql',
                    'pov-ray',
                    'powershell',
                    'powertoys',
                    'prestashop',
                    'primer',
                    'privacy',
                    'probot',
                    'product-management',
                    'producthunt',
                    'programming-language',
                    'project-management',
                    'psr-7',
                    'publishing',
                    'pug',
                    'pulsar',
                    'puppet',
                    'purescript',
                    'puzzle-game',
                    'pwa',
                    'pycharm',
                    'python',
                    'pytorch',
                    'qmk',
                    'qt',
                    'quantum-computing',
                    'quarkus',
                    'quarto',
                    'r',
                    'racing-game',
                    'racing-simulator',
                    'racket',
                    'rails',
                    'raku',
                    'raspberry-pi',
                    'ratchet',
                    'react',
                    'react-native',
                    'react-router',
                    'reactiveui',
                    'reactphp',
                    'real-time-strategy',
                    'real-time-tactics',
                    'reason',
                    'red',
                    'reddit',
                    'redis',
                    'redux',
                    'reflex-frp',
                    'remarkable-tablet',
                    'replit',
                    'rest-api',
                    'retro-game',
                    'retrocomputing',
                    'reverse-engineering',
                    'rhythm-game',
                    'riot-games',
                    'riot-os',
                    'riscv',
                    'robotframework',
                    'robotics',
                    'rocket',
                    'rocketseat',
                    'rockset',
                    'roguelike',
                    'roguelite',
                    'role-playing-game',
                    'roomba',
                    'rpc',
                    'rss',
                    'ruby',
                    'rust',
                    'sailfishos',
                    'saltstack',
                    'sandstorm',
                    'sanitization',
                    'sas',
                    'sass',
                    'satellite',
                    'sbml',
                    'scala',
                    'scambaiting',
                    'scapy',
                    'scikit',
                    'scikit-learn',
                    'scipy',
                    'sciter',
                    'sdk',
                    'sdl',
                    'sdn',
                    'security',
                    'selenium',
                    'self-hosted',
                    'seo',
                    'server',
                    'server-side-rendering',
                    'serverless',
                    'service-fabric',
                    'shadowsocks',
                    'sharex',
                    'shell',
                    'shoot-em-up',
                    'shooter',
                    'sidekiq',
                    'simulator',
                    'sitecore',
                    'sketch',
                    'slack',
                    'social-simulator',
                    'socket-io',
                    'software-challenge-germany',
                    'solana',
                    'solidity',
                    'soundcloud',
                    'space-flight-simulator',
                    'spacetraders',
                    'spacevim',
                    'spacy',
                    'spark',
                    'sports-game',
                    'spotify',
                    'spring',
                    'spring-boot',
                    'sql',
                    'sql-server',
                    'sqlite',
                    'squeak',
                    'sre',
                    'ss13',
                    'stackoverflow',
                    'stackql',
                    'standard-ml',
                    'stata',
                    'static-code-analysis',
                    'statistics',
                    'stealth-game',
                    'steam',
                    'steganography',
                    'stem',
                    'stimulus',
                    'storybook',
                    'strategy-game',
                    'streamlit',
                    'styled-components',
                    'sublime-text',
                    'suckless',
                    'supabase',
                    'support',
                    'survival',
                    'survival-horror',
                    'svelte',
                    'svg',
                    'swift',
                    'swiftui',
                    'swing',
                    'symfony',
                    'syntax-highlighting',
                    'synthetic-biology',
                    't3-stack',
                    'tactical-role-playing',
                    'tactical-shooter',
                    'tailwind',
                    'tas',
                    'taskfile',
                    'tauri',
                    'tbox',
                    'teamfight-tactics',
                    'teeworlds',
                    'telegram',
                    'tensorflow',
                    'terminal',
                    'termux',
                    'terraform',
                    'test',
                    'testing',
                    'tex',
                    'text-adventure',
                    'thelounge',
                    'third-person-shooter',
                    'threejs',
                    'tic-80',
                    'tiktok',
                    'time-management-game',
                    'tldr',
                    'toit',
                    'tower-defense',
                    'tree-sitter',
                    'turn-based',
                    'turn-based-strategy',
                    'turn-based-tactics',
                    'tutorial',
                    'tuya',
                    'tvos',
                    'twitch',
                    'twitter',
                    'twrp',
                    'typescript',
                    'ubuntu',
                    'uefi',
                    'ui',
                    'ui-design',
                    'ukagaka',
                    'umbraco',
                    'unigine',
                    'unist',
                    'unity',
                    'university-of-texas-arlington',
                    'unreal-engine',
                    'unrealscript',
                    'uportal',
                    'uri-template',
                    'userscript',
                    'utau',
                    'utility',
                    'uwp',
                    'v',
                    'vagrant',
                    'vala',
                    'valorant',
                    'vanilla-js',
                    'vapor',
                    'vba',
                    'vehicle-simulator',
                    'vehicular-combat',
                    'vercel',
                    'vertx',
                    'video',
                    'vim',
                    'virtual-reality',
                    'visual-basic',
                    'visual-novel',
                    'visual-studio',
                    'visual-studio-code',
                    'vite',
                    'viur',
                    'vk',
                    'vm-box',
                    'vpn',
                    'vr-game',
                    'vrchat',
                    'vscode-extension',
                    'vue',
                    'vut',
                    'wagtail',
                    'wargame',
                    'watchos',
                    'web',
                    'web-accessibility',
                    'web-assembly',
                    'web-components',
                    'web-monetization',
                    'webapp',
                    'webauthn',
                    'webextension',
                    'webkit',
                    'webpack',
                    'website',
                    'websocket',
                    'webview',
                    'webxr',
                    'whatsapp',
                    'whisper',
                    'wiki',
                    'windows',
                    'windows-subsystem-for-android',
                    'winforms',
                    'winui',
                    'woodpeckerci',
                    'wordplate',
                    'wordpress',
                    'wow',
                    'wpf',
                    'wsl',
                    'xamarin',
                    'xampp',
                    'xcode',
                    'xk6',
                    'xmake',
                    'xml',
                    'xmpp',
                    'xonsh',
                    'xontrib',
                    'yaml',
                    'yarn',
                    'yii',
                    'youtube',
                    'zeit',
                    'zephyr-rtos',
                    'zeplin',
                    'zeronet',
                    'zig',
                    'zip',
                    'zsh',
                    'zustand',
                    'zx-spectrum'}

    topicToLanMap = {"cpp": "c++", "csharp": "c#"}
    lanToTopicMap = {"c++": "cpp", "c#": "csharp"}
