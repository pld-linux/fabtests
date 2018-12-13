Summary:	Test suite for libfabric API
Summary(pl.UTF-8):	Zestaw testów dla API libfabric
Name:		fabtests
Version:	1.6.2
Release:	1
License:	BSD or GPL v2
Group:		Libraries
#Source0Download: https://github.com/ofiwg/fabtests/releases
Source0:	https://github.com/ofiwg/fabtests/releases/download/v%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	55388de12ac75c899296265d5581b620
URL:		https://github.com/ofiwg/fabtests
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.11
BuildRequires:	libfabric-devel >= 1.4.1
BuildRequires:	libtool >= 2:2
BuildRequires:	sed >= 4.0
Requires:	libfabric >= 1.4.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fabtests provides a set of examples that uses libfabric - a
high-performance fabric software library.

%description -l pl.UTF-8
Fabtests to zbiór przykładów wykorzystujących libfabric - bibliotekę
wysoko wydajnych usług sieci typu fabric.

%prep
%setup -q

%{__sed} -i -e '1s,/usr/bin/env ruby,/usr/bin/ruby,' scripts/rft_yaml_to_junit_xml

%build
%{__libtoolize}
%{__aclocal} -I config
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# don't package plain unit tests
%{__rm} $RPM_BUILD_ROOT%{_bindir}/fi_{av_test,cm_data,cntr_test,cq_data,cq_test,dgram,dgram_waitset,dom_test,eq_test,getinfo_test,mr_test,msg,msg_epoll,msg_rma,msg_sockets,poll,rdm,rdm_atomic,rdm_rma_*,rdm_multi_recv,rdm_rma,rdm_tagged_peek,scalable_ep,shared_ctx}
%{__rm} $RPM_BUILD_ROOT%{_bindir}/runfabtests.sh

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING
%attr(755,root,root) %{_bindir}/fi_av_xfer
%attr(755,root,root) %{_bindir}/fi_cmatose
%attr(755,root,root) %{_bindir}/fi_dgram_pingpong
%attr(755,root,root) %{_bindir}/fi_inj_complete
%attr(755,root,root) %{_bindir}/fi_mcast
%attr(755,root,root) %{_bindir}/fi_multi_ep
%attr(755,root,root) %{_bindir}/fi_multi_mr
%attr(755,root,root) %{_bindir}/fi_msg_bw
%attr(755,root,root) %{_bindir}/fi_msg_pingpong
%attr(755,root,root) %{_bindir}/fi_msg_stream
%attr(755,root,root) %{_bindir}/fi_rc_pingpong
%attr(755,root,root) %{_bindir}/fi_rdm_cntr_pingpong
%attr(755,root,root) %{_bindir}/fi_rdm_deferred_wq
%attr(755,root,root) %{_bindir}/fi_rdm_multi_domain
%attr(755,root,root) %{_bindir}/fi_rdm_pingpong
%attr(755,root,root) %{_bindir}/fi_rdm_shared_av
%attr(755,root,root) %{_bindir}/fi_rdm_tagged_bw
%attr(755,root,root) %{_bindir}/fi_rdm_tagged_pingpong
%attr(755,root,root) %{_bindir}/fi_recv_cancel
%attr(755,root,root) %{_bindir}/fi_resmgmt_test
%attr(755,root,root) %{_bindir}/fi_resource_freeing
%attr(755,root,root) %{_bindir}/fi_rma_bw
%attr(755,root,root) %{_bindir}/fi_ubertest
%attr(755,root,root) %{_bindir}/fi_unexpected_msg
%attr(755,root,root) %{_bindir}/rft_yaml_to_junit_xml
%{_datadir}/fabtests
%{_mandir}/man7/fabtests.7*
