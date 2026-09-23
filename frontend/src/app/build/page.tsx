import { redirect } from 'next/navigation';

// The city builder is now at /setup. This file exists only to redirect
// any old /build links so they still work.
export default function BuildPage() {
  redirect('/setup');
}
