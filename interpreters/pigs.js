let variables = {0: 0};
let waiting = false;
let inp = undefined;
let commands, c, pv;
let interval;

function run() {
    let i, j, J;
    let b = false;
    document.getElementById("status").innerHTML = "Running...";
    if (commands)
    interval = setInterval(() => {
        if (c < commands.length) {
            i = commands[c][0];
            j = commands[c].substring(1, commands[c].length);
            j = parseInt(j, 2);
            initvar(j);
            J = variables[j];
            switch (i) {
                case "P":
                    try {
                        output(String.fromCodePoint(J));
                    } catch {}
                    break;
                case "I":
                    if (inp === undefined) {
                        if (!waiting) {
                            output('<textarea class="input" rows="1" cols="5"></textarea><button id="submit" onclick="sub();" onchange="">Submit</button>');
                            waiting = true;
                        }
                    } else {
                        for (var k = 0; k < inp.length; k++) {
                            idx = J + k;
                            clamp(idx);
                            variables[idx] = inp.codePointAt(k);
                        }
                        inp = undefined;
                    }
                    break;
                case "G":
                    c = J - 1;
                    break;
                case "S":
                    pv = J;
                    initvar(pv);
                    break;
                case "+":
                    variables[pv] += J;
                    clamp(variables[pv]);
                    break;
                case "-":
                    variables[pv] -= J;
                    clamp(variables[pv]);
                    break;
                case "=":
                    variables[pv] = Number(variables[pv] === J);
                    break;
                case ":":
                    initvar(J);
                    variables[pv] = variables[J];
                    break;
                case "#":
                    variables[pv] = j;
                    clamp(variables[pv]);
                    break;
            }
            if (!waiting) {
                c++;
            } else {
                b = true;
                document.getElementById("status").innerHTML = "Waiting for input...";
            }
        } else {
            b = true;
            document.getElementById("status").innerHTML = "";
        }
        if (b) {clearInterval(interval); b = false;}
    }, 0);
}

function sub() {
    let inputs = document.getElementsByClassName("input");
    let input = inputs[inputs.length - 1];
    input.readOnly = true;
    input.classList.add("inputted")
    input.innerHTML = input.value;
    inp = input.value;
    waiting = false;
    document.getElementById("submit").remove()
    run();
}

function reset() {
    document.getElementById("output").innerHTML = "";
    variables = {0: 0};
    commands = document.getElementById("program").value.replace(/[^PIGS+-=:#01]/g, "").match(/([PIGS+-=:#])([01]+)/g);
    c = 0;
    pv = 0;
}

function output(x) {
    out = document.getElementById("output");
    document.getElementById("output").innerHTML += x;
    out.scrollTop = out.scrollHeight;
}

let initvar = v => {if (!Object.keys(variables).includes(v.toString())) variables[v] = 0;}
let clamp = n => {n = n % (2 ** 32);}