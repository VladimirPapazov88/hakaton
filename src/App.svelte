<script>
	export var type = "certproject"

	function certproject() {
		type = "certproject"
	}
	function teacher() {
		type = "teacher"
	}
	function jury() {
		type = "jury"
	}
</script>

<svelte:head>
	<title>Автоматизатор дипломов</title>
	<script
		src="https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.5.0/semantic.min.js"
		integrity="sha512-Xo0Jh8MsOn72LGV8kU5LsclG7SUzJsWGhXbWcYs2MAmChkQzwiW/yTQwdJ8w6UA9C6EVG18GHb/TrYpYCjyAQw=="
		crossorigin="anonymous"
		referrerpolicy="no-referrer"
	></script>
	<link
		rel="stylesheet"
		href="https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.5.0/semantic.min.css"
		integrity="sha512-KXol4x3sVoO+8ZsWPFI/r5KBVB/ssCGB5tsv2nVOKwLg33wTFP3fmnXa47FdSVIshVTgsYk/1734xSk9aFIa4A=="
		crossorigin="anonymous"
		referrerpolicy="no-referrer"
	/>
	<script
		src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.1.81/pdf.min.js"
		integrity="sha512-RV+l/3iMDTmIt64ztJmriqLRZl2IwGHcG+655gFxUa20Uq9GljEsY3wibq5BZkGzRlMbYFHUPelVQvWvZxP38w=="
		crossorigin="anonymous"
		referrerpolicy="no-referrer"
	></script>
</svelte:head>

<main>
	<div class="ui stackable menu">
		<div class="item gr">Автоматизатор дипломов</div>
		<!-- svelte-ignore a11y-missing-attribute -->
		{#if type == "certproject"}
			<!-- svelte-ignore a11y-missing-attribute -->
			<a class="item active" on:click={certproject}>Сертификат для проекта</a>
			<!-- svelte-ignore a11y-click-events-have-key-events -->
			<a class="item" on:click={teacher}>Благодарность научному руководителю</a>
			<!-- svelte-ignore a11y-click-events-have-key-events -->
			<a class="item" on:click={jury}>Благодарность жюри</a>
		{:else if type == "teacher"}
			<!-- svelte-ignore a11y-missing-attribute -->
			<a class="item" on:click={certproject}>Сертификат для проекта</a>
			<!-- svelte-ignore a11y-click-events-have-key-events -->
			<a class="item active" on:click={teacher}>Благодарность научному руководителю</a>
			<!-- svelte-ignore a11y-click-events-have-key-events -->
			<a class="item" on:click={jury}>Благодарность жюри</a>
		{:else if type == "jury"}
			<!-- svelte-ignore a11y-missing-attribute -->
			<a class="item" on:click={certproject}>Сертификат для проекта</a>
			<!-- svelte-ignore a11y-click-events-have-key-events -->
			<a class="item" on:click={teacher}>Благодарность научному руководителю</a>
			<!-- svelte-ignore a11y-click-events-have-key-events -->
			<a class="item active" on:click={jury}>Благодарность жюри</a>
		{/if}

	</div>

	<div class="ui equal width center aligned padded grid">
		<div class="column">
			<form action="/generate" method="post">
				<div class="ui input">
					<input type="text" placeholder="ФИО" name="name">
				</div>
				{#if type == "certproject"}
					<div class="ui input">
						<input type="text" placeholder="Название проекта" name="project">
					</div>
				{/if}
				<input type="hidden" name="type" value="{type}">
				<br>
				<br>
				<button type="submit" class="ui labeled icon button teal">Создать и скачать<i class="copy icon"></i></button>
			</form>
		</div>
		<div class="column bl">
			<img class="pdf" src="1.jpg" />
		</div>
		
	</div>
</main>

<style>
	.gr {
		background-color: rgb(47, 177, 163) !important;
		color: white !important;
	}

	.pdf {
		height: 47rem;
		border-radius: 10px;
	}
</style>
