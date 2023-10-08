const ctx2 = document.getElementById("myChart2");

const plugin2 = {
  id: "customCanvasBackgroundColor",
  beforeDraw: (chart, args, options) => {
    const { ctx } = chart; // Corrigido para ctx
    ctx.save();
    ctx.globalCompositeOperation = "destination-over";
    ctx.fillStyle = options.color || "#fff";
    ctx.fillRect(0, 0, chart.width, chart.height);
    ctx.restore();
  },
};

const url = "http://127.0.0.1:8000/rendas/api/v1/rendas/";

fetch(url, {
  method: "GET",
  credentials: "include",
  headers: {
    "Content-Type": "application/json",
  },
})
  .then((response) => response.json())
  .then((data) => {
    const totalsByType = data.reduce((acc, item) => {
      if (!acc[item.tipo]) {
        acc[item.tipo] = 0;
      }
      acc[item.tipo] += item.valor;
      return acc;
    }, {});
    const labels = Object.keys(totalsByType);
    const values = labels.map((label) =>
      parseFloat(totalsByType[label].toFixed(2))
    );

    // Cores correspondentes à nova paleta
    const backgroundColors = [
      "#02C39A", // Primary
      "#7B2CBF", // Accent
      "#495057", // Neutral Dark Gray
      "#DEE2E6", // Neutral Light Gray
      "#D8D9FA", // Neutral Light
      "#007f5f",
      "#55a630",
      "#80b918",
      "#aacc00",
      "#bfd200",
      "#d4d700",
      "#dddf00",
      "#eeef20",
      "#ffff3f",
    ].slice(0, labels.length);

    new Chart(ctx2, {
      // Deve ser ctx2, não ctx
      type: "bar",
      data: {
        labels: labels,
        datasets: [
          {
            label: "Valor R$",
            data: values,
            borderWidth: 1,
            backgroundColor: backgroundColors,
          },
        ],
      },
      options: {
        plugins: {
          title: {
            display: true,
            text: "Valor por Renda",
          },
        },
        scales: {
          y: {
            beginAtZero: true,
            backdropColor: "#111111",
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
      plugins: [plugin2],
    });
  });
