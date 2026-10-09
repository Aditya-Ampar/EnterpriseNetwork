import subprocess

def run_test(h1,h2,h3):
    h3.cmd('iperf -s > /tmp/server.log 2>$1 &')

    p1 = h1.popen(
            'iperf -c 10.0.0.3 -t 20',
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
            )

    p2 = h2.popen(
            'iperf -c 10.0.0.3 -t 20',
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
            )

    out1 = p1.communicate()[0].decode()
    out2 = p2.communicate()[0].decode()

    print("======= H1 ========")
    print(out1)

    print("======= H2 ========")
    print(out2)


