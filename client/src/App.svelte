<script>
	import L from 'leaflet'

	export let name;
</script>

<main>
	<nav class="bg-blue-900 shadow-lg">
		<div class="container mx-auto">
			<div class="sm:flex">
				<a href="/" class="text-white text-3xl font-bold p-3">{name}</a>
				
				<!-- Menus  -->
				<!--
				<div class="ml-55 mt-4">
					<ul class="text-white sm:self-center text-xl">
						<li class="sm:inline-block">
							<a href="#" class="p-3 hover:text-red-900">About</a>
						</li>
						<li class="sm:inline-block">
							<a href="#" class="p-3 hover:text-red-900">Services</a>
						</li>
						<li class="sm:inline-block">
							<a href="#" class="p-3 hover:text-red-900">Blog</a>
						</li>
						<li class="sm:inline-block">
							<a href="#" class="p-3 hover:text-red-900">Contact</a>
						</li>
					</ul>
				</div>
				-->
			</div>
		</div>
	</nav>
</main>

<style global lang="postcss">
	@tailwind base;
	@tailwind components;
	@tailwind utilities;
</style>
  
<!--
<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>
-->