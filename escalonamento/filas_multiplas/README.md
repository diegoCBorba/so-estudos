<div>
    <h1>Múltiplas Filas</h1>
    <p>Nesse código criei um programa que simula o <strong>escalonamento de processos</strong> fazendo uso de <strong>múltiplas filas</strong></p>
    <hr>
    <p>Algumas características do escalonamento de múltiplas filas:</p>
    <ul>
        <li>Sistema Interativo</li>
        <li>Preemptivo</li>
        <li>Cada vez que um processo é executado e suspenso, ele recebe mais tempo para execução</li>
        <li>Inicialmente recebe 1 quantum, e é suspenso</li>
        <li>Então muda de classe e recebe 2, sendo suspenso</li>
        <li>Reduz o número de trocas de processo</li>
        <li>Os mais curtos terminam logo</li>
        <li>Aos mais longos é dado mais tempo, progressivamente</li>
    </ul>
    <p><strong>OBS:</strong> A cada mudança de classe aumentei o quantum em 4 para
ficar mais ditático no código</p>
</div>
