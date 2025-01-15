<script>
    import Version1 from "./components/Version1.svelte";
    import Version2 from "./components/Version2.svelte";

    const params = new URLSearchParams(window.location.search);
    const version = params.get('v') ?? params.get('version') ?? '1';

    const versions = {
      '1': Version1,
      '2': Version2,
    };

    console.log('version:', version);
</script>

<div class="bg-gray-300 h-screen p-5">
  <svelte:component this={versions[version] ?? Version1} />
</div>