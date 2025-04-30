import 'package:client/data/blocs/plaid_link/plaid_link_bloc.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter_bloc/flutter_bloc.dart';

class BlocProviders extends StatelessWidget
{
  BlocProviders();

  @override
  Widget build( BuildContext context )
  {
    return MultiBlocProvider(
        providers: [
          BlocProvider(
              lazy: false,
              create: (context) => PlaidLinkBloc()
          )
        ],
        child: Container() ///TODO add the child widget here, this will be the main screen of the app.
    );
  }
}