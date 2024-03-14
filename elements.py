'''
All the combination of items and items are present in the file
The items are sorted in alphabetical order
'''

elements = {
    "1UP": [
        ["🧬 life", "🍄 mushroom"]
    ],
    "🌬️ air": [], # [] means its a basic element
    "✈️ airplane": [
        ["🌬️ air", "🚗 car"],
        ["🐦 bird", "🔗 metal"]
    ],
    "🤓 Albert Einstein": [
      ["⚡ energy", "🧑‍🔬 scientist"]  
    ],
    "🍷 alchohol": [
        ["🍷 alchohol", "🦠 bacteria"],
        ["🔥 fire", "🌬️ air"]
    ],
    "🍻 alcholic": [
        ["🍷 alchohol", "🧑 man"],
        ["🍺 beer", "🧑 man"],
        ["🧑 man", "🍸 vodka"],
        ["🧑 man", "🍹 tequila"]
    ],
    "🌱 algae": [
        ["🧬 life", "💧 water"]
    ],
    "👽 alien" : [
        ["👹 beast", "⭐ star"],
        ["🧬 life", "⭐ star"]
    ],
    "🔩 aluminium": [
        ["✈️ airplane", "🔗 metal"],
        ["🪶 feather", "🔗 metal"]
    ],
    "🚑 ambulance": [
        ["🚗 car", "🏥 hospital"],
        ["🚗 car", "🤒 sick"]
    ],
    "🐟 aquarium": [
        ["🐠 fish", "🪟 glass"]
    ],
    "🌿 arable": [
        ["🌎 earth", "🛠️ tool"]
    ],
    "💪 arms": [
        ["🔗 metal", "🛠️ tool"]
    ],
    "🌫 ash": [
        ["📕 book", "🔥 fire"],
        ["🚬 cigarettes", "🔥 fire"],
        ["⚰️ corpse", "🔥 fire"],
        ["🐉 dragon", "🛖 hut"],
        ["🐉 dragon", "🧑 man"],
        ["🐉 dragon", "🧑🏹 hunter"],
        ["🌳 ent", "🔥 fire"],
        ["🔥 fire elementa", "💧 water"],
        ["🔥 fire", "🛖 hut"],
        ["🔥 fire", "🌿 moss"],
        ["🔥 fire", "📄 paper"],
        ["🔥 fire", "🐍 snake"],
        ["🔥 fire", "🚬 tobacco"],
        ["🔥 fire", "🌳 tree"],
        ["🔥 fire", "🪵 wood"],
        ["🔥 fire", "🐛 worm"],
        ["🌋 lava", "🧑 man"],
        ["🌋 lava", "👩 woman"],
        ["💡 light", "🧛 vampire"],
        ["🗜 pressure", "🌋 volcano"],
        ["☀️ Sun", "🧛 vampire"],
        ["💨 dust", "💨 dust"]
    ],
    "🪣 ashtray": [
        ["🌫 ash", "🪟 glass"]
    ],
    "🥷🏻 assasin": [
        ["🥷🏻 assasin", "🧑 man"],
        ["🥷🏻 assasin", "👩 woman"],
        ["🧑 man", "🧪🗡️ poisoned weapon"]
    ],
    "🇦🇺 Australia": [
        ["🗺 continent", "🌏 country"],
        ["🌏 country", "🦘 kangaroo"]
    ],
    "🐦🤒 avian flu": [
        ["🐦 bird", "🤒 flu"],
        ["🐓 chicken", "🤒 flu"]
    ],
    "👶 baby": [
        ["🧬 life", "❤️ sex"],
        ["🧬 life", "👩 woman"],
        ["🧑 man", "❤️ sex"],
        ["❤️ sex", "👩 woman"]
    ],
    "🥓 bacon": [
        ["🔥 fire", "🐷 pig"]
    ],
    "🦠 bacteria": [
        ["🧬 life", "🏞️ swamp"],
        ["🧬 life", "💩 mud"]
    ],
    "🥂🏠 bar": [
        ["🍺 beer", "🧱🏠 brick house"],
        ["🍹 tequila", "🧱🏠 brick house"],
        ["🍸 vodka", "🧱🏠 brick house"]
    ],
    "♨️ barbeque": [
        ["🔥 fire", "🥩 meat"]
    ],
    "🦇 bat": [
        ["🐦 bird", "🧛 vampire"]
    ],
    "🦸‍♂️🦇 Batman": [
        ["🦇 bat", "🦸‍♂ hero"],
        ["🦇 bat", "🧑 man"]
    ],
    "🏝️ beach": [
        ["🏜️ sand", "☀️ Sun"],
        ["🏜️ sand", "💧 water"]
    ],
    "🐻 bear": [
        ["👹 beast", "🌲🌳 forest"],
        ["👹 beast", "🍯 honey"]
    ],
    "👹 beast": [
        ["👹 beast", "💨 oxygen"],
        ["🌎 earth", "🦎 lizard"],
        ["🌲🌳 forest", "🧬 life"]
    ],
    "🦫 beaver": [
        ["👹 beast", "🌊 dam"]
    ],
    "🐝 bee": [
        ["🐞 1le", "🌸 flower"],
        ["🌸 flower", "🧑🏹 hunter"]
    ],
    "🍺 beer": [
        ["🍷 alchohol", "🍞 bread"],
        ["🍷 alchohol", "🌾 wheat"]
    ],
    "🐞 beetle": [
        ["🌎 earth", "🐛 worm"]
    ],
    "🟣🥕 beetroot": [
        ["🌾 reed", "🧑‍🔬 scientist"],
        ["🍚 sugar", "🫘 seed"]
    ],
    "🇧🇾 Belarus": [
      ["🌏 country", "🚜 tractor"]  
    ],
    "🍓 berry": [
        ["🍎 fruit", "🌿 grass"]
    ],
    "🚲 bicycle": [
        ["🛞 wheel", "🛞 wheel"]
    ],
    "🐦 bird": [
        ["💨 air", "🥚 egg"],
        ["💨 air", "🦎 lizard"]
        ["🐦 bird", "🐛 worm"],
        ["🐦 bird", "🐦 bird"]
    ],
    "🛢 bitumen": [
        ["🛢 kerogen", "🗜 pressure"]
    ],
    "🩸 blood": [
        ["🍻 alcholic", "🚗 car"],
        ["👹 beast", "🧑🏹 hunter"],
        ["👹 beast", "🥷 warrior"],
        ["🐦 bird", "🧑🏹 hunter"],
        ["🦖 dinosaur", "🧑🏹 hunter"],
        ["🦖 dinosaur", "🧑 man"],
        ["🦖 dinosaur", "🥷 warrior"],
        ["🐉 dragon", "🥷 warrior"]
        ["🧑 man", "🥷 warrior"]
    ],
    "⛵ boat": [
        ["💧 water", "🪵 wood"]
    ],
    "🌡️ boiler": [
        ["🔗 metal", "💨 steam"]
    ],
    "📕 book": [
        ["🪶 feather", "📄 paper"],
        ["🧑 man", "📄 paper"]
    ],
    "🍛 borscht": [
        ["🟣🥕 beetroot", "🔥 fire"],
        ["🟣🥕 beetroot", "🥩 meat"],
        ["🟣🥕 beetroot", "🍖 salo"]
    ],
    "🎀 bow": [
        ["💪 arms", "🏹 Robin Hood"]
    ],
    "🍞 bread": [
        ["🥟 dough", "🔥 fire"]
    ],
    "🧱 brick": [
        ["⚱️ clay", "🔥 fire"]
    ],
    "🧱🏠 brick house": [
        ["🧱 brick", "🪨 concrete"]
    ],
    "🦋 butterfly": [
        ["🌬️ air", "🐛 worm"],
        ["🕟 time", "🐛 worm"]
    ],
    "🇩🇪 Germany": [
        ["🌏 country", "🚗 VW Beetle"]
    ],
    "🇷🇴 Romania": [
        ["🌏 country", "Transylvania"],
        ["🕟 time", "Transylvania"]
    ],
    "🇮🇳 India": [
        ["🌏 country", "📕 Kama Sutra"]
    ]
}
