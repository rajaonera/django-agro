create or replace function public.create_profile_if_not_exists(uid uuid, email text)
returns void
language plpgsql
security definer
set search_path = public
as $$
begin
  -- Vérifie si un profil avec ce user_id existe déjà
  if not exists (
    select 1 from public.profiles where user_id = uid
  ) then
    -- S'il n'existe pas, on le crée
    insert into public.profiles (user_id, email)
    values (uid, email);
  end if;
end;
$$;


