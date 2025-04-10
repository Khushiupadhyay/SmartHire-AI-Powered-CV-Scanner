window.onload = async () => {
    try {
      const res = await fetch('http://127.0.0.1:5000/jobs');
      const jobs = await res.json();
  
      const jobList = document.getElementById("job-list");
      const buttonPanel = document.getElementById("scan-buttons");
  
      jobs.forEach(job => {
        const jobDiv = document.createElement("div");
        jobDiv.className = "job-card";
        jobDiv.innerHTML = `<strong>${job}</strong>`;
        jobList.appendChild(jobDiv);
  
        const btnDiv = document.createElement("div");
        btnDiv.className = "job-card";
        btnDiv.innerHTML = `
          <button onclick="scanJob('${job}')">📥 Scan CVs for <strong>${job}</strong></button>
        `;
        buttonPanel.appendChild(btnDiv);
      });
  
    } catch (error) {
      document.getElementById("output").innerHTML = "❌ Failed to load jobs. Is backend running?";
    }
  };
  
  async function scanJob(job) {
    const output = document.getElementById("output");
    output.innerHTML = `🔍 Scanning CVs for <strong>${job}</strong>...`;
  
    const res = await fetch("http://127.0.0.1:5000/scan", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ job })
    });
  
    const result = await res.json();
  
    if (result.shortlisted?.length > 0) {
      const list = result.shortlisted.map(c => `<li>${c.name} – <strong>${c.score}%</strong></li>`).join('');
      output.innerHTML = `
        <h3>✅ Shortlisted for <strong>${job}</strong>:</h3>
        <ul>${list}</ul>
        <p>📧 Emails sent!</p>
      `;
    } else {
      output.innerHTML = `😕 No CVs matched for <strong>${job}</strong>.`;
    }
  }
  