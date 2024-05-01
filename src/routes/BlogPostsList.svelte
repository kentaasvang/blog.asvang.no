<script>

	const posts = {
		"Title 1": ["the first paragraph", ""],
		"Title 2": ["the second paragraph", "img source"],
	}

</script>


<div class="container mx-auto">

	<div class="md:px-20 sm:px-5 mx-auto">
	
		<div class="md:w-1/2 mx-auto">

			<!-- for each post in posts! -->

			{#each Object.entries(posts) as [title, [paragraph, img_src]]}

				<div class="flex flex-row border border-1 border-black">

					<div class="basis-1/4">

						{#if img_src != ""}

							<p>{img_src}</p>

							<img src="{img_src}" alt="">

						{/if}

					</div>

					<div class="basis-3/4">

						<h1 class="font-bold">{title}</h1>

						<p>{paragraph}</p>

					</div>

				</div>

			{/each}

			<!-- end for loop -->
		</div>

	</div>

</div>
