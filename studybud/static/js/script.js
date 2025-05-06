const dropdown = document.getElementById("dropdown");
const showSettings = document.getElementById("show-settings");

if (dropdown) {
	dropdown.addEventListener("click", () => {
		showSettings.classList.add("show");
	});
}
