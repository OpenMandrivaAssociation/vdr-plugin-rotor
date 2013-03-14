
%define plugin	rotor
%define name	vdr-plugin-%plugin
%define version	0.1.4
%define rel	19

Summary:	VDR plugin: DiseqC motor steering
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://home.vrweb.de/~bergwinkl.thomas/
Source:		vdr-%plugin-%version-vdr1.5.7.tgz
Patch0:		vdr-rotor-0.1.4-fix-crash.patch
Patch1:		92_Rotor-0.1.4-vdr1.5.10.dpatch
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
With this plugin you can control a diseqc motor.

%prep
%setup -q -n %plugin-%version
%patch0 -p1 -b .crash
%patch1 -p1
%vdr_plugin_prep

%build
%vdr_plugin_build

%install
%vdr_plugin_install

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY




%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.1.4-18mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Sat Mar 21 2009 Anssi Hannula <anssi@mandriva.org> 0.1.4-17mdv2009.1
+ Revision: 359770
- rediff crash-fix patch
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.1.4-16mdv2009.0
+ Revision: 197972
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.1.4-15mdv2009.0
+ Revision: 197717
- switch to 1.5.7 flavor
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- adapt for api changes of VDR 1.5.10 (P1 from e-tobi)

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.1.4-14mdv2008.1
+ Revision: 145196
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.1.4-13mdv2008.1
+ Revision: 103197
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.1.4-12mdv2008.0
+ Revision: 50040
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.1.4-11mdv2008.0
+ Revision: 42126
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.1.4-10mdv2008.0
+ Revision: 22678
- rebuild for new vdr


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.1.4-9mdv2007.0
+ Revision: 90968
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.1.4-8mdv2007.1
+ Revision: 74079
- rebuild for new vdr
- Import vdr-plugin-rotor

* Sat Sep 23 2006 Anssi Hannula <anssi@mandriva.org> 0.1.4-7mdv2007.0
- patch0: fix crash due to an invalid pointer (Johan Schuring)

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.1.4-6mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.1.4-5mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.1.4-4mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.1.4-3mdv2007.0
- rebuild for new vdr

* Tue Jun 20 2006 Anssi Hannula <anssi@mandriva.org> 0.1.4-2mdv2007.0
- rebuild for new vdr

* Sat Jun 10 2006 Anssi Hannula <anssi@mandriva.org> 0.1.4-1mdv2007.0
- initial Mandriva release

