import { createClient } from "https://cdn.jsdelivr.net/npm/@supabase/supabase-js/+esm";

const supabaseUrl = Deno.env.get("https://iizemuhywcgfokqkhdoq.supabase.co")!;
const supabaseKey = Deno.env.get("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlpemVtdWh5d2NnZm9rcWtoZG9xIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc0OTExODI0NiwiZXhwIjoyMDY0Njk0MjQ2fQ.k6osOVlIC3fGPKW2A_BsoWpx9Mdy3fOplu6S_exhMVc")!;
const supabase = createClient(supabaseUrl, supabaseKey);

Deno.serve(async (req) => {
  try {
    const { uid, email } = await req.json();

    // Appel à la fonction RPC SQL stockée dans Supabase
    const { data, error } = await supabase.rpc("create_profile_if_not_exists", { uid, email });

    if (error) {
      return new Response(JSON.stringify({ error: error.message }), { status: 400, headers: { "Content-Type": "application/json" } });
    }

    return new Response(JSON.stringify({ message: "Profil créé ou confirmé.", data }), { status: 200, headers: { "Content-Type": "application/json" } });

  } catch (err) {
    return new Response(JSON.stringify({ error: err.message }), { status: 500, headers: { "Content-Type": "application/json" } });
  }
});
