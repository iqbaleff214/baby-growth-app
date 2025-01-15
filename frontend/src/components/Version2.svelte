<div class="max-w-96 mx-auto bg-white rounded-lg shadow p-5 flex flex-col gap-y-6">
    <div class="flex flex-col gap-y-3">
      <div class="flex flex-col gap-y-2">
        <label for="ultrasound">Ultrasound Picture</label>
        <input type="file" id="ultrasound" accept="image/*">
      </div>
      <div class="flex flex-col gap-y-2">
        <label for="father">Father Picture</label>
        <input type="file" id="father" accept="image/*">
      </div>
      <div class="flex flex-col gap-y-2">
        <label for="mother">Mother Picture</label>
        <input type="file" id="mother" accept="image/*">
      </div>
    </div>
    <div>
      <button 
        type="button"
        class="px-4 py-2 bg-blue-500 text-white font-semibold rounded-lg shadow-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-300">
        Proceed
      </button>

      <p class="text-xs text-center text-gray-400 mt-5">v2</p>
    </div>
</div>