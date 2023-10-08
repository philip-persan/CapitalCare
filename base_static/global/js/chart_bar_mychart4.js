const ctx4 = document.getElementById("myChart4");

const plugin4 = {
  id: "customCanvasBackgroundColor",
  beforeDraw: (chart, args, options) => {
    const { ctx } = chart; // Corrigir para ctx
    ctx.save();
    ctx.globalCompositeOperation = "destination-over";
    ctx.fillStyle = options.color || "#fff";
    ctx.fillRect(0, 0, chart.width, chart.height);
    ctx.restore();
  },
};

const url4 = "http://127.0.0.1:8000/investimentos/api/v1/annotations/"; // URL correta

fetch(url4, {
  method: "GET",
  credentials: "include",
  headers: {
    "Content-Type": "application/json",
  },
})
  .then((response) => response.json())
  .then((data) => {
    const totalsByAtivo = data.por_ativo;
    const labels = totalsByAtivo.map((item) => item.ativo);
    const values = totalsByAtivo.map((item) =>
      parseFloat(item.total_por_ativo)
    );

    new Chart(ctx4, {
      type: "bar",
      data: {
        labels: labels,
        datasets: [
          {
            label: "Valor R$",
            data: values,
            borderWidth: 1,
            backgroundColor: [
              "#02C39A", // Primary
              "#7B2CBF", // Accent
              "#495057", // Neutral Dark Gray
              "#DEE2E6", // Neutral Light Gray
              "#D8D9FA", // Neutral Light
            ],
          },
        ],
      },
      options: {
        plugins: {
          title: {
            display: true,
            text: "Investimentos por Ativo",
          },
        },
        scales: {
          y: {
            beginAtZero: true,
            ticks: {
              color: "black",
            },
          },
          x: {
            grid: {
              tickColor: "black",
            },
            ticks: {
              color: "black",
            },
          },
          tickWidth: 3,
        },
        backgroundColor: "rgba(0, 0, 0, 0)",
      },
      plugins: [plugin4],
    });
  });
