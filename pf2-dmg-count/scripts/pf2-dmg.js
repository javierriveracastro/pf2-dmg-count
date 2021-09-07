// Initialization file for pf2-dmg-count

Hooks.on("init", function () {
    console.log("PF2-DMG-COUNT Brython version javascript loader running");
    $("body").append("<script id='pyloader' type='text/python' src='/modules/pf2-dmg-count/scripts/main.py'>");
    brython({debug:1, ids:['pyloader'], pythonpath: ['/modules/pf2-dmg-count/scripts/']});
})