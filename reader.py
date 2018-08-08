import ctypes
import keyboard
import time
import pyautogui as pag

def round_to_dp(num, dp):
    return int(num * (10*dp)) / (10*dp) 

while not keyboard.is_pressed('['):
    pass

start = time.time()

actions = [{'move': (929, 717), 'press': ['['], 'time': 0.0}, {'release': ['['], 'time': 0.07880020141601562}, {'press': ['left windows'], 'time': 0.6989350318908691}, {'release': ['left windows'], 'time': 0.7989208698272705}, {'press': ['n'], 'time': 1.1789023876190186}, {'press': ['o'], 'time': 1.259202241897583}, {'release': ['n'], 'time': 1.3290152549743652}, {'press': ['t'], 'time': 1.378394365310669}, {'release': ['o'], 'time': 1.4053235054016113}, {'press': ['e'], 'time': 1.440229892730713}, {'release': ['t'], 'time': 1.4980738162994385}, {'release': ['e'], 'time': 1.5788583755493164}, {'press': ['enter'], 'time': 1.8391609191894531}, {'release': ['enter'], 'time': 1.8890297412872314}, {'press': ['g'], 'time': 3.4288108348846436}, {'release': ['g'], 'time': 3.5188541412353516}, {'press': ['g'], 'time': 3.580688714981079}, {'release': ['g'], 'time': 3.649266242980957}, {'press': ['g'], 'time': 3.6987171173095703}, {'release': ['g'], 'time': 3.789476156234741}, {'press': ['g'], 'time': 3.8393406867980957}, {'release': ['g'], 'time': 3.9188711643218994}, {'press': ['g'], 'time': 3.948791027069092}, {'release': ['g'], 'time': 4.039548635482788}, {'press': ['g'], 'time': 4.079454660415649}, {'release': ['g'], 'time': 4.179685354232788}, {'press': ['a'], 'time': 4.3183183670043945}, {'press': ['r'], 'time': 4.389461994171143}, {'release': ['a'], 'time': 4.43900990486145}, {'release': ['r'], 'time': 4.489873647689819}, {'press': ['t'], 'time': 4.589731931686401}, {'release': ['t'], 'time': 4.678493976593018}, {'press': ['g'], 'time': 4.918094158172607}, {'press': ['a'], 'time': 5.029802322387695}, {'release': ['g'], 'time': 5.068690776824951}, {'release': ['a'], 'time': 5.15976619720459}, {'press': ['n'], 'time': 5.168740749359131}, {'press': ['t'], 'time': 5.288914442062378}, {'release': ['n'], 'time': 5.289897203445435}, {'release': ['t'], 'time': 5.3886399269104}, {'press': ['backspace'], 'time': 5.8392956256866455}, {'release': ['backspace'], 'time': 6.338579177856445}, {'press': ['backspace'], 'time': 6.371491193771362}, {'release': ['backspace'], 'time': 6.404403448104858}, {'press': ['backspace'], 'time': 6.438311338424683}, {'release': ['backspace'], 'time': 6.4712607860565186}, {'press': ['backspace'], 'time': 6.505150318145752}, {'release': ['backspace'], 'time': 6.537079811096191}, {'press': ['backspace'], 'time': 6.569998264312744}, {'release': ['backspace'], 'time': 6.602909803390503}, {'press': ['backspace'], 'time': 6.635664701461792}, {'release': ['backspace'], 'time': 6.668573617935181}, {'press': ['backspace'], 'time': 6.702482461929321}, {'release': ['backspace'], 'time': 6.73440408706665}, {'press': ['backspace'], 'time': 6.768308877944946}, {'release': ['backspace'], 'time': 6.801217794418335}, {'press': ['backspace'], 'time': 6.834130764007568}, {'release': ['backspace'], 'time': 6.8670430183410645}, {'press': ['backspace'], 'time': 6.899955749511719}, {'release': ['backspace'], 'time': 6.932866811752319}, {'press': ['backspace'], 'time': 6.96577787399292}, {'release': ['backspace'], 'time': 6.998691558837891}, {'press': ['backspace'], 'time': 7.031603813171387}, {'release': ['backspace'], 'time': 7.064515590667725}, {'press': ['backspace'], 'time': 7.0974280834198}, {'release': ['backspace'], 'time': 7.130341053009033}, {'press': ['backspace'], 'time': 7.158263921737671}, {'press': ['1'], 'time': 7.42854118347168}, {'release': ['1'], 'time': 7.518301010131836}, {'press': ['enter'], 'time': 7.818497896194458}, {'release': ['enter'], 'time': 7.928203582763672}, {'press': ['2'], 'time': 8.189887523651123}, {'release': ['2'], 'time': 8.279651403427124}, {'press': ['2'], 'time': 8.358710050582886}, {'release': ['2'], 'time': 8.45944094657898}, {'press': ['enter'], 'time': 8.678852558135986}, {'release': ['enter'], 'time': 8.768622636795044}, {'press': ['3'], 'time': 8.939170598983765}, {'release': ['3'], 'time': 8.998378276824951}, {'press': ['3'], 'time': 9.109565019607544}, {'release': ['3'], 'time': 9.189349889755249}, {'press': ['3'], 'time': 9.279109239578247}, {'release': ['3'], 'time': 9.379153490066528}, {'press': ['enter'], 'time': 9.688989162445068}, {'release': ['enter'], 'time': 9.789719820022583}, {'press': ['4'], 'time': 9.969150304794312}, {'release': ['4'], 'time': 10.468183279037476}, {'press': ['4'], 'time': 10.501518726348877}, {'release': ['4'], 'time': 10.535428047180176}, {'press': ['4'], 'time': 10.567689180374146}, {'release': ['4'], 'time': 10.60156774520874}, {'press': ['4'], 'time': 10.633487701416016}, {'release': ['4'], 'time': 10.667404413223267}, {'press': ['4'], 'time': 10.699325799942017}, {'release': ['4'], 'time': 10.732217788696289}, {'press': ['4'], 'time': 10.76613187789917}, {'release': ['4'], 'time': 10.799039602279663}, {'press': ['4'], 'time': 10.832115411758423}, {'release': ['4'], 'time': 10.866017580032349}, {'press': ['4'], 'time': 10.898927688598633}, {'release': ['4'], 'time': 10.93092679977417}, {'press': ['4'], 'time': 10.96383786201477}, {'release': ['4'], 'time': 10.996749877929688}, {'press': ['4'], 'time': 11.018818140029907}]
time_passed = 0
for action in actions:
    time_passed = time.time() - start
    while not time_passed > action['time']:
        time_passed = time.time() - start
        time.sleep(0.01)

    if 'left click' in action:
        pag.click(button='left')
        
    if 'right click' in action:
        pag.click(button='right')
        
    if 'move' in action:
        pag.moveTo(action['move'])
        
    if 'press' in action:
        for key_pressed in action['press']:
            keyboard.press(key_pressed)

    if 'release' in action:
        for key_released in action['release']:
            keyboard.release(key_released)
